# Agentic - AI-Based Adaptive Learning Platform

## Overview
Agentic is an AI-based adaptive learning platform designed specifically for differently abled students. The platform provides accessibility features, multimodal AI interaction, adaptive learning logic, and a clean dashboard UI.

## Project Goals
- Personalizes learning material based on each student's ability
- Supports voice, text, sign language detection, and visual interaction
- Adapts difficulty level using rule-based logic
- Tracks student behavior, progress, and performance
- Provides a simple, accessible web UI

## Tech Stack
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, Feather Icons
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Speech Recognition**: SpeechRecognition library
- **Charts**: Matplotlib
- **Data Processing**: NumPy, Pandas

## Project Structure
```
/
├── main.py                 # Application entry point
├── app.py                  # Flask app configuration
├── routes.py               # All Flask routes
├── models.py               # Database models
├── seed_data.py            # Database seeding script
├── /modules/               # Core functionality modules
│   ├── tts_engine.py       # Text-to-Speech
│   ├── stt_engine.py       # Speech-to-Text
│   ├── sign_language_detector.py
│   ├── adaptive_engine.py  # Learning adaptation logic
│   ├── content_personalization.py
│   ├── emotion_detector.py
│   └── progress_tracker.py
├── /utils/                 # Utility functions
│   ├── helpers.py          # General helpers
│   └── plot_utils.py       # Chart generation
├── /templates/             # HTML templates
│   ├── base.html           # Base layout
│   ├── index.html          # Login page
│   ├── register.html       # Registration
│   ├── dashboard.html      # Main dashboard
│   ├── lesson.html         # Lesson viewer
│   ├── quiz.html           # Quiz interface
│   ├── quiz_result.html    # Results page
│   ├── progress.html       # Analytics
│   ├── settings.html       # User settings
│   ├── help.html           # Help & accessibility
│   └── error.html          # Error pages
├── /static/
│   ├── /css/style.css      # Main stylesheet
│   └── /audio/             # Generated TTS audio
└── design_guidelines.md    # UI/UX guidelines
```

## Key Features

### Accessibility Features
- **Text-to-Speech**: Audio playback for lesson content
- **High Contrast Mode**: For visually impaired users
- **Large Font Options**: Adjustable font sizes (14-24px)
- **Reduce Motion**: Disable animations
- **Keyboard Navigation**: Full keyboard support
- **Sign Language Mode**: Gesture-based navigation (placeholder)

### Adaptive Learning
- Three difficulty levels: Easy, Medium, Advanced
- Automatic difficulty adjustment based on quiz performance
- Personalized content for each level
- Progress tracking and recommendations

### Analytics
- Quiz score tracking
- Progress charts (Matplotlib)
- Weekly activity reports
- Achievement badges
- Personalized recommendations

## Database Models
- **Student**: User profiles with accessibility settings
- **Lesson**: Learning content at three difficulty levels
- **Quiz**: Assessment questions per lesson/difficulty
- **QuizQuestion**: Individual questions with options
- **QuizResult**: Student quiz performance
- **LessonProgress**: Lesson completion tracking
- **EmotionLog**: Emotion detection records
- **ActivityLog**: User activity tracking

## Running the Application
The application runs on port 5000 using Gunicorn:
```
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

## Seeding Data
Run the seed script to populate sample lessons and quizzes:
```
python seed_data.py
```

## Demo Account
- Student ID: DEMO001
- Name: Demo Student

## Recent Changes
- December 2024: Initial MVP implementation
  - Created complete Flask application structure
  - Implemented all accessibility modules
  - Built responsive, accessible UI
  - Added adaptive quiz system
  - Created progress analytics with charts

## User Preferences
- Accessibility-first design
- WCAG AAA compliance where possible
- Atkinson Hyperlegible font for readability
- Touch-friendly targets (min 48px)
- Clear visual feedback for all interactions
