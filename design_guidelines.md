# Design Guidelines: Agentic AI Adaptive Learning Platform

## Design Approach: Accessibility-First Material Design

**Rationale:** Material Design 3 provides comprehensive accessibility guidelines, WCAG AAA compliance patterns, and robust component systems essential for differently abled users. This system prioritizes clarity, predictability, and adaptability—critical for our diverse user base.

**Core Principles:**
- Maximum readability and clarity over aesthetics
- Consistent, predictable interaction patterns
- Touch-friendly targets (minimum 48px)
- Clear visual feedback for all interactions
- Support for keyboard-only navigation

## Typography System

**Font Family:** 
- Primary: Atkinson Hyperlegible (Google Fonts) - specifically designed for low vision readers
- Fallback: Inter or Roboto

**Scale (Desktop):**
- Hero/Headers: 3rem (48px), font-weight: 700
- Section Titles: 2rem (32px), font-weight: 600
- Body Large: 1.25rem (20px), font-weight: 400
- Body Standard: 1.125rem (18px), font-weight: 400
- Small/Captions: 1rem (16px), font-weight: 400

**Mobile Scale:** Reduce by 25% for smaller viewports

**Line Height:** 1.6 minimum for all body text, 1.3 for headings

**Critical:** Never use font sizes below 16px. All text must pass WCAG AAA standards.

## Layout & Spacing System

**Tailwind Units:** Consistently use 4, 6, 8, 12, 16, 20 as primary spacing increments
- Component padding: p-6 to p-8
- Section spacing: py-12 to py-20
- Card gaps: gap-6 to gap-8
- Form field spacing: space-y-6

**Grid System:**
- Dashboard: Single column mobile, 2-column tablet (md:), 3-column desktop (lg:) for cards
- Lessons/Quiz: Single column with max-w-4xl centering
- Progress Analytics: 2-column grid for charts

**Container Strategy:**
- Main content: max-w-7xl mx-auto px-6
- Reading content: max-w-3xl mx-auto
- Forms: max-w-2xl mx-auto

## Component Library

### Navigation
**Top Navigation Bar:**
- Fixed position with z-50
- Height: h-20 (80px) for large touch targets
- Student name/ID display on left
- Mode indicators (Audio/Sign/Emotion) as large icon buttons
- Logout button on right
- Voice command status indicator

### Dashboard Cards
**Student Profile Card:**
- Large profile picture (128px circle)
- Student name in 2rem
- Quick stats grid (lessons completed, current level, streak)
- Primary CTA: "Continue Learning"

**Lesson Cards:**
- Minimum height: h-40
- Left border accent (8px width) indicating difficulty level
- Large lesson title
- Progress bar showing completion
- Time estimate and difficulty badge
- Click entire card to enter

**Progress Charts:**
- Card container with p-8
- Chart title above
- Matplotlib-generated charts as responsive images
- Clear legend with large text
- Time period selector (Week/Month/All)

### Forms & Input

**Quiz Interface:**
- Question number indicator (large, "Question 3 of 10")
- Question text in 1.5rem with generous line-height
- Multiple choice options as full-width cards (h-16 minimum)
- Clear selected state with thick border
- Navigation buttons: Previous/Next/Submit (large, w-40 minimum)
- Timer display (if applicable) - large, non-distracting

**Input Fields:**
- Height: h-14 (56px) minimum
- Font size: 1.125rem
- Clear labels above inputs
- Visible focus states with thick outlines
- Voice input button integrated into text fields

### Accessibility Controls Panel

**Mode Switcher (Prominent):**
- Large toggle buttons in horizontal row
- Icons + text labels for: Text Mode / Audio Mode / Sign Language Mode / Emotion Detection
- Active state clearly indicated
- Minimum button size: 120px × 80px

### Lesson Viewer

**Content Area:**
- Maximum width: max-w-3xl for optimal reading
- Generous padding: p-8 to p-12
- Audio playback controls: Large play/pause buttons (64px)
- Text simplification toggle
- Font size adjuster (+/- buttons, current size display)
- Content sections separated with py-8

**Sign Language Video Panel:**
- Side-by-side layout on desktop (60/40 split)
- Stack on mobile
- Video player with large controls
- Synchronized highlighting of current text

### Progress & Analytics

**Weekly Report Card:**
- Header with week range
- 4-column stats grid: Quizzes Taken / Average Score / Time Spent / Difficulty Level
- Line chart showing progress trend
- Achievement badges section
- Recommendations panel

### Emotion Detection Interface

**Webcam Panel:**
- Camera feed in 16:9 aspect ratio
- Overlay indicators: Engagement meter, Detected emotion
- Privacy notice and toggle switch
- Minimal UI during lessons to avoid distraction

## Animation Guidelines

**Strictly Minimal:**
- Page transitions: Simple fade (200ms)
- Button feedback: Scale 0.98 on press
- Loading states: Simple spinner, no complex animations
- NO scroll-triggered animations
- NO parallax effects
- Card hover: Subtle lift (2px) only

**Critical:** Provide "Reduce Motion" toggle that disables ALL animations.

## Images

**Hero Section (Dashboard):**
- No traditional hero image
- Start directly with personalized greeting and mode selector
- Welcoming illustration (abstract, inclusive) as page header background (max 200px height)

**Lesson Content:**
- Inline diagrams and visual aids embedded within text
- Alt text mandatory for all images
- High contrast, simple graphics
- Icon library: Material Icons via CDN

**Imagery Approach:** Functional graphics that enhance comprehension, never decorative. Use illustrations showing diverse students, assistive technologies, and learning scenarios.

## Responsive Behavior

**Breakpoints:**
- Mobile-first approach
- sm: 640px (stack all columns)
- md: 768px (2-column layouts begin)
- lg: 1024px (3-column dashboard, side panels appear)

**Touch Targets:** All interactive elements minimum 48px × 48px on all devices.

This platform prioritizes function over form, ensuring every student can learn effectively regardless of ability.