"""
Flask Routes for Agentic AI Learning Platform
"""
import os
import logging
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db, login_manager
from models import Student, Lesson, Quiz, QuizQuestion, QuizResult, LessonProgress, EmotionLog, ActivityLog

from modules.tts_engine import text_to_speech, generate_lesson_audio
from modules.stt_engine import stt_engine, get_voice_commands
from modules.sign_language_detector import sign_language_detector
from modules.adaptive_engine import adaptive_engine
from modules.content_personalization import content_personalizer
from modules.emotion_detector import emotion_detector
from modules.progress_tracker import progress_tracker

from utils.helpers import (
    format_time_spent, format_date_relative, get_difficulty_color,
    get_difficulty_label, get_score_message, get_greeting,
    get_progress_bar_class, get_accessibility_options, generate_student_id
)
from utils.plot_utils import (
    create_score_line_chart, create_difficulty_pie_chart,
    create_progress_bar_chart, create_weekly_activity_chart
)

logger = logging.getLogger(__name__)


@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))


@app.context_processor
def utility_processor():
    """Add utility functions to template context"""
    return {
        'format_time_spent': format_time_spent,
        'format_date_relative': format_date_relative,
        'get_difficulty_color': get_difficulty_color,
        'get_difficulty_label': get_difficulty_label,
        'get_progress_bar_class': get_progress_bar_class,
        'get_greeting': get_greeting,
    }


@app.route('/')
def index():
    """Landing page / Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    students = Student.query.order_by(Student.name).all()
    return render_template('index.html', students=students)


@app.route('/login', methods=['POST'])
def login():
    """Handle student login"""
    student_id = request.form.get('student_id')
    password = request.form.get('password', '')
    
    if not student_id:
        flash('Please select a student profile.', 'error')
        return redirect(url_for('index'))
    
    student = Student.query.filter_by(student_id=student_id).first()
    
    if not student:
        flash('Student not found.', 'error')
        return redirect(url_for('index'))
    
    if student.password_hash and not student.check_password(password):
        flash('Invalid password. Please try again.', 'error')
        return redirect(url_for('index'))
    
    login_user(student)
    progress_tracker.update_streak(student, db.session)
    
    activity = ActivityLog(
        student_id=student.id,
        activity_type='login',
        details='Student logged in'
    )
    db.session.add(activity)
    db.session.commit()
    
    flash(f'Welcome back, {student.name}!', 'success')
    return redirect(url_for('dashboard'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register new student"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not name:
            flash('Please enter your name.', 'error')
            return redirect(url_for('register'))
        
        if len(name) > 100:
            flash('Name is too long. Please use a shorter name.', 'error')
            return redirect(url_for('register'))
        
        if email:
            if len(email) > 120:
                flash('Email is too long.', 'error')
                return redirect(url_for('register'))
            existing = Student.query.filter_by(email=email).first()
            if existing:
                flash('This email is already registered.', 'error')
                return redirect(url_for('register'))
        
        student_id = generate_student_id()
        while Student.query.filter_by(student_id=student_id).first():
            student_id = generate_student_id()
        
        student = Student(
            student_id=student_id,
            name=name,
            email=email if email else None,
            current_difficulty='easy'
        )
        
        if password:
            student.set_password(password)
        
        db.session.add(student)
        db.session.commit()
        
        login_user(student)
        flash(f'Welcome, {name}! Your student ID is {student_id}. Save it for future logins.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    """Logout current user"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard"""
    lessons = Lesson.query.filter_by(is_active=True).order_by(Lesson.order_index).all()
    
    lesson_progress_list = LessonProgress.query.filter_by(student_id=current_user.id).all()
    quiz_results = QuizResult.query.filter_by(student_id=current_user.id).all()
    
    progress_stats = progress_tracker.calculate_lesson_progress(
        current_user, lessons, lesson_progress_list
    )
    
    performance = adaptive_engine.analyze_performance(current_user.id, quiz_results)
    
    recommendations = adaptive_engine.get_personalized_recommendations(
        current_user, performance
    )
    
    progress_map = {lp.lesson_id: lp for lp in lesson_progress_list}
    
    return render_template('dashboard.html',
        student=current_user,
        lessons=lessons,
        progress_map=progress_map,
        progress_stats=progress_stats,
        performance=performance,
        recommendations=recommendations,
        accessibility_options=get_accessibility_options()
    )


@app.route('/lesson/<int:lesson_id>')
@login_required
def lesson(lesson_id):
    """View a lesson"""
    lesson = Lesson.query.get_or_404(lesson_id)
    
    difficulty = current_user.current_difficulty
    content = content_personalizer.get_content_for_level(lesson, difficulty)
    
    lesson_progress = LessonProgress.query.filter_by(
        student_id=current_user.id,
        lesson_id=lesson_id
    ).first()
    
    if not lesson_progress:
        lesson_progress = LessonProgress(
            student_id=current_user.id,
            lesson_id=lesson_id,
            status='in_progress',
            started_at=datetime.utcnow(),
            difficulty_used=difficulty
        )
        db.session.add(lesson_progress)
    else:
        lesson_progress.status = 'in_progress'
        lesson_progress.last_accessed = datetime.utcnow()
    
    db.session.commit()
    
    content_formats = content_personalizer.get_content_formats(content, lesson_id)
    
    audio_url = None
    if current_user.audio_enabled:
        audio_url = generate_lesson_audio(content, lesson_id, difficulty)
    
    quiz = Quiz.query.filter_by(lesson_id=lesson_id, difficulty=difficulty).first()
    
    activity = ActivityLog(
        student_id=current_user.id,
        activity_type='lesson_view',
        details=f'Viewed lesson: {lesson.title}'
    )
    db.session.add(activity)
    db.session.commit()
    
    all_lessons = Lesson.query.filter_by(is_active=True).order_by(Lesson.order_index).all()
    current_index = next((i for i, l in enumerate(all_lessons) if l.id == lesson_id), 0)
    prev_lesson = all_lessons[current_index - 1] if current_index > 0 else None
    next_lesson = all_lessons[current_index + 1] if current_index < len(all_lessons) - 1 else None
    
    return render_template('lesson.html',
        lesson=lesson,
        content=content,
        content_formats=content_formats,
        lesson_progress=lesson_progress,
        audio_url=audio_url,
        quiz=quiz,
        difficulty=difficulty,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson,
        voice_commands=get_voice_commands()
    )


@app.route('/lesson/<int:lesson_id>/complete', methods=['POST'])
@login_required
def complete_lesson(lesson_id):
    """Mark a lesson as completed"""
    lesson_progress = LessonProgress.query.filter_by(
        student_id=current_user.id,
        lesson_id=lesson_id
    ).first()
    
    if lesson_progress:
        lesson_progress.status = 'completed'
        lesson_progress.progress_percent = 100
        lesson_progress.completed_at = datetime.utcnow()
        
        current_user.total_lessons_completed += 1
        
        db.session.commit()
        flash('Lesson completed! Great job!', 'success')
    
    lesson = Lesson.query.get(lesson_id)
    quiz = Quiz.query.filter_by(
        lesson_id=lesson_id, 
        difficulty=current_user.current_difficulty
    ).first()
    
    if quiz:
        return redirect(url_for('take_quiz', quiz_id=quiz.id))
    
    return redirect(url_for('dashboard'))


@app.route('/quiz/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    """Take a quiz"""
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = QuizQuestion.query.filter_by(quiz_id=quiz_id).order_by(QuizQuestion.order_index).all()
    
    if not questions:
        flash('This quiz has no questions yet.', 'warning')
        return redirect(url_for('dashboard'))
    
    activity = ActivityLog(
        student_id=current_user.id,
        activity_type='quiz_start',
        details=f'Started quiz for lesson {quiz.lesson_id}'
    )
    db.session.add(activity)
    db.session.commit()
    
    session['quiz_start_time'] = datetime.utcnow().timestamp()
    
    return render_template('quiz.html',
        quiz=quiz,
        questions=questions,
        lesson=quiz.lesson,
        total_questions=len(questions),
        voice_commands=get_voice_commands()
    )


@app.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    """Submit quiz answers"""
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = QuizQuestion.query.filter_by(quiz_id=quiz_id).all()
    
    correct_count = 0
    answers = {}
    
    for question in questions:
        answer = request.form.get(f'question_{question.id}')
        answers[question.id] = answer
        
        if answer and answer.upper() == question.correct_answer.upper():
            correct_count += 1
    
    total = len(questions)
    score = (correct_count / total * 100) if total > 0 else 0
    
    start_time = session.get('quiz_start_time', datetime.utcnow().timestamp())
    time_spent = int(datetime.utcnow().timestamp() - start_time)
    
    quiz_result = QuizResult(
        student_id=current_user.id,
        quiz_id=quiz_id,
        score=score,
        total_questions=total,
        correct_answers=correct_count,
        time_spent=time_spent,
        difficulty_at_time=current_user.current_difficulty
    )
    db.session.add(quiz_result)
    
    current_user.total_quizzes_taken += 1
    
    all_results = QuizResult.query.filter_by(student_id=current_user.id).all()
    all_scores = [r.score for r in all_results] + [score]
    current_user.average_score = sum(all_scores) / len(all_scores)
    
    recent_results = QuizResult.query.filter_by(
        student_id=current_user.id
    ).order_by(QuizResult.completed_at.desc()).limit(5).all()
    
    should_adjust, new_difficulty, reason = adaptive_engine.should_adjust_difficulty(
        current_user, recent_results + [quiz_result]
    )
    
    difficulty_changed = False
    if should_adjust and new_difficulty != current_user.current_difficulty:
        old_difficulty = current_user.current_difficulty
        current_user.current_difficulty = new_difficulty
        difficulty_changed = True
    
    db.session.commit()
    
    session.pop('quiz_start_time', None)
    
    return render_template('quiz_result.html',
        quiz=quiz,
        questions=questions,
        answers=answers,
        score=score,
        correct_count=correct_count,
        total=total,
        time_spent=time_spent,
        difficulty_changed=difficulty_changed,
        new_difficulty=new_difficulty if difficulty_changed else None,
        message=get_score_message(score)
    )


@app.route('/progress')
@login_required
def progress():
    """View progress and analytics"""
    quiz_results = QuizResult.query.filter_by(
        student_id=current_user.id
    ).order_by(QuizResult.completed_at.desc()).all()
    
    lessons = Lesson.query.filter_by(is_active=True).all()
    lesson_progress_list = LessonProgress.query.filter_by(student_id=current_user.id).all()
    activity_logs = ActivityLog.query.filter_by(student_id=current_user.id).all()
    
    quiz_stats = progress_tracker.calculate_quiz_statistics(quiz_results)
    
    lesson_stats = progress_tracker.calculate_lesson_progress(
        current_user, lessons, lesson_progress_list
    )
    
    weekly_report = progress_tracker.get_weekly_report(
        current_user, quiz_results, lesson_progress_list, activity_logs
    )
    
    chart_data = progress_tracker.get_progress_chart_data(quiz_results)
    
    score_chart = None
    if chart_data['line_chart']['scores']:
        valid_scores = [s for s in chart_data['line_chart']['scores'] if s is not None]
        if valid_scores:
            score_chart = create_score_line_chart(
                chart_data['line_chart']['labels'],
                chart_data['line_chart']['scores']
            )
    
    difficulty_chart = None
    if chart_data['difficulty_distribution']['values']:
        difficulty_chart = create_difficulty_pie_chart(
            chart_data['difficulty_distribution']['labels'],
            chart_data['difficulty_distribution']['values']
        )
    
    activity_chart = None
    if weekly_report['daily_activity']:
        activity_chart = create_weekly_activity_chart(
            list(weekly_report['daily_activity'].keys()),
            list(weekly_report['daily_activity'].values())
        )
    
    performance = adaptive_engine.analyze_performance(current_user.id, quiz_results)
    recommendations = adaptive_engine.get_personalized_recommendations(current_user, performance)
    
    return render_template('progress.html',
        student=current_user,
        quiz_stats=quiz_stats,
        lesson_stats=lesson_stats,
        weekly_report=weekly_report,
        performance=performance,
        recommendations=recommendations,
        score_chart=score_chart,
        difficulty_chart=difficulty_chart,
        activity_chart=activity_chart
    )


@app.route('/settings')
@login_required
def settings():
    """User settings page"""
    return render_template('settings.html',
        student=current_user,
        accessibility_options=get_accessibility_options()
    )


@app.route('/settings/update', methods=['POST'])
@login_required
def update_settings():
    """Update user settings"""
    current_user.audio_enabled = request.form.get('audio_enabled') == 'on'
    current_user.sign_language_enabled = request.form.get('sign_language_enabled') == 'on'
    current_user.emotion_detection_enabled = request.form.get('emotion_detection_enabled') == 'on'
    current_user.high_contrast = request.form.get('high_contrast') == 'on'
    current_user.reduce_motion = request.form.get('reduce_motion') == 'on'
    
    font_size = request.form.get('font_size', '18')
    try:
        current_user.font_size = int(font_size)
    except ValueError:
        current_user.font_size = 18
    
    db.session.commit()
    flash('Settings updated successfully!', 'success')
    return redirect(url_for('settings'))


@app.route('/api/tts', methods=['POST'])
@login_required
def api_tts():
    """Generate TTS audio for text"""
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    audio_url = text_to_speech(text)
    
    if audio_url:
        return jsonify({'audio_url': audio_url})
    return jsonify({'error': 'Failed to generate audio'}), 500


@app.route('/api/emotion', methods=['POST'])
@login_required
def api_emotion():
    """Log detected emotion"""
    data = request.get_json()
    emotion = data.get('emotion', 'neutral')
    confidence = data.get('confidence', 0.5)
    context = data.get('context', 'lesson')
    
    result = emotion_detector.process_emotion(emotion, confidence, current_user.id)
    
    emotion_log = EmotionLog(
        student_id=current_user.id,
        emotion=emotion,
        confidence=confidence,
        context=context
    )
    db.session.add(emotion_log)
    db.session.commit()
    
    return jsonify(result)


@app.route('/help')
def help_page():
    """Help and accessibility information"""
    return render_template('help.html',
        voice_commands=get_voice_commands(),
        gesture_mappings=sign_language_detector.get_gesture_mappings(),
        asl_alphabet=sign_language_detector.get_asl_alphabet(),
        accessibility_options=get_accessibility_options()
    )


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('error.html', 
        error_code=404, 
        error_message='Page not found'
    ), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('error.html',
        error_code=500,
        error_message='Something went wrong. Please try again.'
    ), 500
