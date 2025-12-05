"""
Seed data script for Agentic AI Learning Platform
Run this to populate the database with sample lessons and quizzes
"""
from app import app, db
from models import Student, Lesson, Quiz, QuizQuestion


def seed_lessons():
    """Create sample lessons"""
    lessons_data = [
        {
            'title': 'Introduction to Numbers',
            'description': 'Learn about numbers and counting from 1 to 10',
            'subject': 'Mathematics',
            'estimated_time': 10,
            'order_index': 1,
            'content_easy': """Welcome to Numbers!

Numbers are all around us. We use them every day to count things.

Let's start with counting from 1 to 10:
1 - One (like one apple)
2 - Two (like two eyes)
3 - Three (like three colors in a traffic light)
4 - Four (like four legs on a dog)
5 - Five (like five fingers on one hand)

Now let's count from 6 to 10:
6 - Six
7 - Seven
8 - Eight
9 - Nine
10 - Ten

Great job! You now know the numbers from 1 to 10.

Remember: Numbers help us count and measure things in our world.""",
            'content_medium': """Understanding Numbers: A Foundation

Numbers are the building blocks of mathematics. They help us quantify, measure, and understand the world around us.

In this lesson, we will explore:
1. Natural numbers (1, 2, 3, 4, 5...)
2. How to count objects
3. Number sequences

Natural Numbers:
Natural numbers are the counting numbers we use every day. They start from 1 and continue infinitely.

Examples in daily life:
- Counting money
- Telling time
- Measuring ingredients

Practice Exercise:
Count the objects around you. How many chairs are in your room? How many windows?

Key Concept: Zero
While we start counting from 1, zero (0) represents the absence of quantity. It's an important number in mathematics.""",
            'content_advanced': """Number Theory: An Introduction

Numbers form the foundation of all mathematical concepts. This lesson explores the nature of numbers and their properties.

1. Classification of Numbers:
- Natural Numbers (N): {1, 2, 3, 4, ...}
- Whole Numbers (W): {0, 1, 2, 3, ...}
- Integers (Z): {..., -2, -1, 0, 1, 2, ...}

2. Properties of Natural Numbers:
- Closure Property: The sum of two natural numbers is always a natural number
- Commutative Property: a + b = b + a
- Associative Property: (a + b) + c = a + (b + c)

3. Number Patterns:
Recognizing patterns helps in predicting sequences.
Example: 2, 4, 6, 8, ... (adding 2 each time)

4. Applications:
Numbers are used in science, engineering, finance, and everyday calculations.

Critical Thinking: Consider how our number system evolved. The decimal system we use today was developed over thousands of years."""
        },
        {
            'title': 'Basic Addition',
            'description': 'Learn how to add numbers together',
            'subject': 'Mathematics',
            'estimated_time': 15,
            'order_index': 2,
            'content_easy': """Let's Learn Addition!

Addition means putting things together. We use the plus sign (+).

When we add, we combine numbers to get a bigger number.

Simple Examples:
1 + 1 = 2 (one apple plus one apple equals two apples)
2 + 1 = 3
2 + 2 = 4
3 + 2 = 5

Let's practice:
- If you have 2 toys and get 1 more, you have 3 toys!
- If you have 3 cookies and get 2 more, you have 5 cookies!

Remember: Addition makes numbers bigger.

Tip: You can use your fingers to help count!""",
            'content_medium': """Addition: Combining Quantities

Addition is one of the four basic operations in mathematics. It represents combining two or more quantities.

The Addition Symbol: +
The result of addition is called the SUM.

Basic Addition Facts:
- 5 + 3 = 8
- 7 + 4 = 11
- 6 + 6 = 12

Properties of Addition:
1. Order doesn't matter: 3 + 5 = 5 + 3 = 8
2. Adding zero: Any number + 0 = the same number

Adding Two-Digit Numbers:
When adding larger numbers, we add digits in the same place value.
Example: 23 + 14 = 37
- Add ones: 3 + 4 = 7
- Add tens: 2 + 1 = 3
- Result: 37

Practice Problems:
1. 8 + 5 = ?
2. 15 + 12 = ?
3. 24 + 31 = ?""",
            'content_advanced': """Addition: Mathematical Foundations

Addition is a binary operation that combines two numbers (addends) to produce a sum.

Formal Definition:
For natural numbers a and b, addition is defined recursively:
- a + 0 = a
- a + S(b) = S(a + b), where S is the successor function

Properties of Addition:
1. Commutativity: a + b = b + a
2. Associativity: (a + b) + c = a + (b + c)
3. Identity Element: a + 0 = a
4. Closure: Natural numbers are closed under addition

Multi-Digit Addition Algorithm:
When adding multi-digit numbers, we use place value and carrying:

Example: 847 + 295
  847
+ 295
-----
 1142

Process:
- 7 + 5 = 12 (write 2, carry 1)
- 4 + 9 + 1 = 14 (write 4, carry 1)
- 8 + 2 + 1 = 11

Applications in Real World:
- Financial calculations
- Scientific measurements
- Data aggregation"""
        },
        {
            'title': 'Reading Comprehension',
            'description': 'Learn how to understand what you read',
            'subject': 'English',
            'estimated_time': 12,
            'order_index': 3,
            'content_easy': """Reading is Fun!

When we read, we look at words and understand their meaning.

Tips for Good Reading:
1. Look at the pictures - they help tell the story
2. Read slowly and carefully
3. If you don't know a word, ask for help
4. Think about what is happening

Practice Story:
"The cat sat on the mat. The cat was orange. The cat was happy."

Questions to think about:
- What animal is in the story?
- Where did the cat sit?
- What color was the cat?

Remember: It's okay to read the same thing more than once!""",
            'content_medium': """Reading Comprehension Strategies

Reading comprehension means understanding what you read. Good readers use strategies to help them understand texts better.

Key Strategies:
1. Preview the text - Look at headings and pictures first
2. Ask questions while reading - What is happening? Why?
3. Make connections - How does this relate to what you know?
4. Visualize - Create pictures in your mind
5. Summarize - What were the main points?

Types of Questions:
- Literal: Information directly stated in the text
- Inferential: Information you figure out from clues
- Evaluative: Your opinion about the text

Practice Passage:
"Maria woke up early on Saturday. She packed her bag with a towel, sunscreen, and a sandwich. Her dad loaded the car with beach chairs."

Questions:
1. What day was it? (Literal)
2. Where was Maria going? (Inferential)
3. Do you think she was excited? Why? (Evaluative)""",
            'content_advanced': """Advanced Reading Comprehension

Effective reading comprehension involves multiple cognitive processes working together to construct meaning from text.

Cognitive Processes in Reading:
1. Decoding - Converting written symbols to language
2. Vocabulary Knowledge - Understanding word meanings in context
3. Syntactic Parsing - Understanding sentence structure
4. Inference Making - Drawing conclusions beyond the text
5. Comprehension Monitoring - Checking understanding

Critical Reading Techniques:
- Identify the author's purpose
- Distinguish fact from opinion
- Recognize bias and perspective
- Evaluate evidence and arguments
- Synthesize information from multiple sources

Annotation Strategies:
- Underline main ideas
- Circle unfamiliar vocabulary
- Write margin notes
- Question the text
- Connect to prior knowledge

Metacognitive Awareness:
Skilled readers monitor their comprehension and employ fix-up strategies when understanding breaks down:
- Re-reading
- Adjusting reading speed
- Looking up unfamiliar terms
- Making conscious inferences"""
        }
    ]
    
    for lesson_data in lessons_data:
        existing = Lesson.query.filter_by(title=lesson_data['title']).first()
        if not existing:
            lesson = Lesson(**lesson_data)
            db.session.add(lesson)
    
    db.session.commit()
    print("Lessons seeded successfully!")


def seed_quizzes():
    """Create sample quizzes for each lesson"""
    lessons = Lesson.query.all()
    
    quiz_questions = {
        'Introduction to Numbers': {
            'easy': [
                {
                    'question_text': 'How many fingers do you have on one hand?',
                    'option_a': '3',
                    'option_b': '4',
                    'option_c': '5',
                    'option_d': '6',
                    'correct_answer': 'C',
                    'explanation': 'We have 5 fingers on each hand.'
                },
                {
                    'question_text': 'What number comes after 7?',
                    'option_a': '6',
                    'option_b': '8',
                    'option_c': '9',
                    'option_d': '5',
                    'correct_answer': 'B',
                    'explanation': 'When counting, 8 comes right after 7.'
                },
                {
                    'question_text': 'Which number is the smallest?',
                    'option_a': '5',
                    'option_b': '10',
                    'option_c': '3',
                    'option_d': '1',
                    'correct_answer': 'D',
                    'explanation': '1 is the smallest number when counting from 1 to 10.'
                }
            ],
            'medium': [
                {
                    'question_text': 'What are natural numbers?',
                    'option_a': 'Numbers found in nature',
                    'option_b': 'Counting numbers starting from 1',
                    'option_c': 'Only even numbers',
                    'option_d': 'Negative numbers',
                    'correct_answer': 'B',
                    'explanation': 'Natural numbers are counting numbers: 1, 2, 3, 4, ...'
                },
                {
                    'question_text': 'Which of these is NOT a natural number?',
                    'option_a': '5',
                    'option_b': '100',
                    'option_c': '0',
                    'option_d': '42',
                    'correct_answer': 'C',
                    'explanation': 'Zero is not a natural number. Natural numbers start from 1.'
                },
                {
                    'question_text': 'What comes next in the sequence: 2, 4, 6, 8, ?',
                    'option_a': '9',
                    'option_b': '10',
                    'option_c': '11',
                    'option_d': '12',
                    'correct_answer': 'B',
                    'explanation': 'The pattern adds 2 each time: 2, 4, 6, 8, 10.'
                }
            ],
            'advanced': [
                {
                    'question_text': 'Which set includes all whole numbers?',
                    'option_a': '{1, 2, 3, ...}',
                    'option_b': '{0, 1, 2, 3, ...}',
                    'option_c': '{..., -1, 0, 1, ...}',
                    'option_d': 'Only positive fractions',
                    'correct_answer': 'B',
                    'explanation': 'Whole numbers include zero and all natural numbers: {0, 1, 2, 3, ...}'
                },
                {
                    'question_text': 'What is the commutative property of addition?',
                    'option_a': 'a + b = b + a',
                    'option_b': 'a + 0 = a',
                    'option_c': '(a + b) + c = a + (b + c)',
                    'option_d': 'a - b = b - a',
                    'correct_answer': 'A',
                    'explanation': 'Commutative property means the order of addition does not change the result.'
                }
            ]
        },
        'Basic Addition': {
            'easy': [
                {
                    'question_text': 'What is 2 + 2?',
                    'option_a': '3',
                    'option_b': '4',
                    'option_c': '5',
                    'option_d': '6',
                    'correct_answer': 'B',
                    'explanation': '2 + 2 = 4'
                },
                {
                    'question_text': 'What is 1 + 3?',
                    'option_a': '2',
                    'option_b': '3',
                    'option_c': '4',
                    'option_d': '5',
                    'correct_answer': 'C',
                    'explanation': '1 + 3 = 4'
                },
                {
                    'question_text': 'If you have 3 apples and get 2 more, how many do you have?',
                    'option_a': '4',
                    'option_b': '5',
                    'option_c': '6',
                    'option_d': '7',
                    'correct_answer': 'B',
                    'explanation': '3 + 2 = 5 apples'
                }
            ],
            'medium': [
                {
                    'question_text': 'What is 15 + 12?',
                    'option_a': '25',
                    'option_b': '26',
                    'option_c': '27',
                    'option_d': '28',
                    'correct_answer': 'C',
                    'explanation': '15 + 12 = 27'
                },
                {
                    'question_text': 'What is 8 + 0?',
                    'option_a': '0',
                    'option_b': '8',
                    'option_c': '80',
                    'option_d': '18',
                    'correct_answer': 'B',
                    'explanation': 'Adding zero to any number gives the same number.'
                },
                {
                    'question_text': 'Is 5 + 3 the same as 3 + 5?',
                    'option_a': 'Yes, both equal 8',
                    'option_b': 'No, they are different',
                    'option_c': 'Only sometimes',
                    'option_d': 'Cannot determine',
                    'correct_answer': 'A',
                    'explanation': 'This is the commutative property - order does not matter in addition.'
                }
            ],
            'advanced': [
                {
                    'question_text': 'What is 847 + 295?',
                    'option_a': '1042',
                    'option_b': '1132',
                    'option_c': '1142',
                    'option_d': '1152',
                    'correct_answer': 'C',
                    'explanation': '847 + 295 = 1142 (with carrying)'
                },
                {
                    'question_text': 'Which property states (a + b) + c = a + (b + c)?',
                    'option_a': 'Commutative',
                    'option_b': 'Associative',
                    'option_c': 'Distributive',
                    'option_d': 'Identity',
                    'correct_answer': 'B',
                    'explanation': 'The associative property allows grouping numbers differently.'
                }
            ]
        },
        'Reading Comprehension': {
            'easy': [
                {
                    'question_text': 'In the story, where did the cat sit?',
                    'option_a': 'On the chair',
                    'option_b': 'On the mat',
                    'option_c': 'On the bed',
                    'option_d': 'On the floor',
                    'correct_answer': 'B',
                    'explanation': 'The story says "The cat sat on the mat."'
                },
                {
                    'question_text': 'What helps tell the story when reading?',
                    'option_a': 'Only words',
                    'option_b': 'Only pictures',
                    'option_c': 'Words and pictures',
                    'option_d': 'Nothing',
                    'correct_answer': 'C',
                    'explanation': 'Both words and pictures help us understand stories.'
                }
            ],
            'medium': [
                {
                    'question_text': 'What does "inferential" mean in reading?',
                    'option_a': 'Information directly stated',
                    'option_b': 'Information you figure out from clues',
                    'option_c': 'Your opinion',
                    'option_d': 'Reading out loud',
                    'correct_answer': 'B',
                    'explanation': 'Inferential means drawing conclusions from clues in the text.'
                },
                {
                    'question_text': 'In the practice passage, where was Maria going?',
                    'option_a': 'School',
                    'option_b': 'The park',
                    'option_c': 'The beach',
                    'option_d': 'The store',
                    'correct_answer': 'C',
                    'explanation': 'Clues like towel, sunscreen, and beach chairs tell us she was going to the beach.'
                }
            ],
            'advanced': [
                {
                    'question_text': 'What is metacognitive awareness in reading?',
                    'option_a': 'Reading fast',
                    'option_b': 'Monitoring your own understanding',
                    'option_c': 'Memorizing text',
                    'option_d': 'Reading aloud',
                    'correct_answer': 'B',
                    'explanation': 'Metacognitive awareness means being aware of your own thinking and understanding.'
                },
                {
                    'question_text': 'Which is a fix-up strategy for comprehension?',
                    'option_a': 'Skip difficult parts',
                    'option_b': 'Read faster',
                    'option_c': 'Re-reading the text',
                    'option_d': 'Stop reading',
                    'correct_answer': 'C',
                    'explanation': 'Re-reading is an effective strategy when understanding breaks down.'
                }
            ]
        }
    }
    
    for lesson in lessons:
        if lesson.title in quiz_questions:
            for difficulty, questions in quiz_questions[lesson.title].items():
                existing_quiz = Quiz.query.filter_by(
                    lesson_id=lesson.id, 
                    difficulty=difficulty
                ).first()
                
                if not existing_quiz:
                    quiz = Quiz(lesson_id=lesson.id, difficulty=difficulty)
                    db.session.add(quiz)
                    db.session.flush()
                    
                    for idx, q_data in enumerate(questions):
                        question = QuizQuestion(
                            quiz_id=quiz.id,
                            order_index=idx,
                            **q_data
                        )
                        db.session.add(question)
    
    db.session.commit()
    print("Quizzes seeded successfully!")


def seed_demo_student():
    """Create a demo student account"""
    existing = Student.query.filter_by(student_id='DEMO001').first()
    if not existing:
        student = Student(
            student_id='DEMO001',
            name='Demo Student',
            email='demo@agentic.learn',
            current_difficulty='easy',
            audio_enabled=False,
            sign_language_enabled=False,
            emotion_detection_enabled=False,
            font_size=18
        )
        db.session.add(student)
        db.session.commit()
        print("Demo student created: DEMO001")
    else:
        print("Demo student already exists")


def run_seed():
    """Run all seed functions"""
    with app.app_context():
        seed_lessons()
        seed_quizzes()
        seed_demo_student()
        print("\nDatabase seeded successfully!")
        print("You can log in with the Demo Student (DEMO001) or create a new profile.")


if __name__ == '__main__':
    run_seed()
