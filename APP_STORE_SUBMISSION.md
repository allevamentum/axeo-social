# AXEO — App Store Submission Checklist

## 1. App Store Connect Metadata

### App Name
`Axeo — Eye Training`

### Subtitle (30 chars max)
`Vision exercises & eye tests`

### Promotional Text (170 chars, can be updated without review)
```
Train your eyes in 5 minutes a day. 17 clinically designed exercises, 6 vision tests, and ARKit gaze tracking. Based on AAO & COVD guidelines. Try free today.
```

### Description (4000 chars max)
```
YOUR EYES WORK 16 HOURS A DAY. WHEN DID YOU LAST TRAIN THEM?

7+ hours of daily screen time is straining your eye muscles, reducing your blink rate by 60%, and contributing to chronic digital eye strain. Axeo is the first eye training app built on clinical guidelines from the American Academy of Ophthalmology (AAO) and the College of Optometrists in Vision Development (COVD).

WHAT YOU GET

17 Clinically Designed Exercises
Focus Shift, Figure Eight, Saccades, Convergence, Palming, and 12 more — each targeting specific eye muscle groups. Exercises use real-time Canvas animations to guide your gaze through clinically validated movement patterns.

6 Medical-Grade Vision Tests
- Snellen Visual Acuity — progressive letter chart
- Ishihara Color Vision — 6 plates, clinical colors
- Astigmatism Check — fan dial directional blur detection
- Contrast Sensitivity — fading letter recognition
- Amsler Grid — macular distortion screening
- Dry Eye Assessment — OSDI questionnaire

3 Structured Programs
- Digital Eye Relief (30 days) — for screen workers, 6+ hours/day
- Vision After 40 (45 days) — full eye fitness for presbyopia prevention
- Dry Eye Relief (30 days) — TFOS DEWS II guidelines, tear film restoration

ARKit Eye Tracking
Real-time gaze accuracy scoring using your iPhone's TrueDepth camera. See exactly how well your eyes follow exercise patterns. 10 exercises support camera tracking.

RESULTS IN WEEKS, NOT MONTHS
- Most users feel reduced eye strain within 1-2 weeks
- Progressive difficulty adapts to your improvement
- Session tracking with detailed progress analytics
- Smart 20-20-20 reminders during your workday

ALSO AVAILABLE ON THE WEB
Train on any device at axeo.vision — your progress syncs across platforms. Take free vision tests right in your browser.

FREE TO START
- 6 free exercises
- 2 free vision tests (Snellen + Ishihara)
- 1 free program (Digital Eye Relief)
- 3 free sessions per day

PREMIUM UNLOCKS EVERYTHING
- All 17 exercises
- All 6 vision tests
- All 3 programs
- Unlimited sessions
- Camera eye tracking
- Progress analytics

SUBSCRIPTION OPTIONS
- Weekly: $2.99/week
- Monthly: $5.99/month (7-day free trial)
- Annual: $34.99/year (7-day free trial) — Best value
- Lifetime: $89.99 one-time

IMPORTANT NOTICE
Axeo provides educational eye exercises. It is not a medical device and does not diagnose, treat, cure, or prevent any disease or condition. Results vary. Consult an eye care professional for comprehensive eye exams. Not a substitute for professional medical advice.

Privacy Policy: https://axeo.vision/privacy
Terms of Service: https://axeo.vision/terms
Support: support@axeo.vision
```

### Keywords (100 chars max, comma separated)
```
eye training,eye exercises,vision test,eye strain,digital wellness,eye health,eye care,snellen,20-20-20,dry eye,eye workout,vision therapy,eye yoga,screen time,blink
```

### Category
Primary: `Health & Fitness`
Secondary: `Medical`

### Age Rating
`4+` (no objectionable content)

### Copyright
`2026 Gaji Labs`

### Support URL
`https://axeo.vision/support`

### Marketing URL
`https://axeo.vision`

### Privacy Policy URL
`https://axeo.vision/privacy`

---

## 2. Screenshots Guide

### Required Sizes
- iPhone 6.7" (1290 x 2796) — iPhone 15 Pro Max
- iPhone 6.5" (1284 x 2778) — iPhone 14 Plus
- iPad Pro 12.9" (2048 x 2732) — if supporting iPad

### 5 Screenshot Concepts (Dark Mode)

**Screenshot 1: Hero / Home**
Caption overlay: "Train your eyes in 5 minutes"
Show: Home screen with daily workout card, stats grid

**Screenshot 2: Exercise in Action**
Caption overlay: "17 clinically designed exercises"
Show: Focus Shift exercise running with timer, gaze tracking overlay

**Screenshot 3: Vision Tests**
Caption overlay: "Test your vision — 6 screening tests"
Show: Snellen test in progress with letter display

**Screenshot 4: Programs**
Caption overlay: "3 structured programs up to 45 days"
Show: Digital Eye Relief program with daily plan, progress bar

**Screenshot 5: Results & Analytics**
Caption overlay: "Track your progress"
Show: Session results with improvement charts, achievement badges

### How to Capture
```bash
# Set simulator to dark mode
xcrun simctl ui booted appearance dark

# Launch app in simulator
open -a Simulator

# Wait for app to load, navigate to desired screen
# Take screenshot with Cmd+S in Simulator
# Screenshots save to Desktop by default
```

---

## 3. App Review Notes

```
NOTES FOR REVIEW

Thank you for reviewing Axeo. Here are some helpful details:

1. SUBSCRIPTIONS: Axeo offers Weekly ($2.99), Monthly ($5.99 with 7-day
   trial), Annual ($34.99 with 7-day trial), and Lifetime ($89.99) plans.
   Free tier includes 6 exercises, 2 vision tests, 1 program, and 3
   sessions per day.

2. EYE TRACKING: The ARKit camera feature requires iPhone X or later with
   TrueDepth camera. Grant camera permission when prompted during exercises
   that support tracking. This feature is optional — all exercises work
   without camera access.

3. HEALTH DISCLAIMER: The app displays a medical disclaimer on first launch
   and in the profile section. We do not make medical claims. All exercises
   are educational, based on published AAO/COVD guidelines.

4. TESTING: To test premium features, you may use the sandbox account or
   subscribe to any plan — all include a free trial period.

5. WEB COMPANION: The app has a companion website at axeo.vision where
   users can take free vision tests and do exercises in their browser.
   This is supplementary and not required for app functionality.

No demo account needed — the app is fully functional in free tier.
```

---

## 4. In-App Purchase Setup

### Subscription Group: "Axeo Premium"

| Product ID | Reference Name | Duration | Price | Trial |
|-----------|---------------|----------|-------|-------|
| com.allevamentum.axeo.premium.weekly | Axeo Weekly | 1 week | $2.99 | None |
| com.allevamentum.axeo.premium.monthly | Axeo Monthly | 1 month | $5.99 | 7 days |
| com.allevamentum.axeo.premium.annual | Axeo Annual | 1 year | $34.99 | 7 days |
| com.allevamentum.axeo.premium.lifetime | Axeo Lifetime | Lifetime | $89.99 | None |

### Subscription Description (for each)
```
Weekly: Unlock all 17 exercises, 6 vision tests, 3 programs, ARKit eye tracking, unlimited sessions, and progress analytics. Billed $2.99 every 7 days.

Monthly: Unlock all 17 exercises, 6 vision tests, 3 programs, ARKit eye tracking, unlimited sessions, and progress analytics. Includes 7-day free trial. Billed $5.99 monthly.

Annual: Unlock all 17 exercises, 6 vision tests, 3 programs, ARKit eye tracking, unlimited sessions, and progress analytics. Includes 7-day free trial. Billed $34.99 annually ($2.92/mo).

Lifetime: One-time purchase. Unlock all current and future exercises, tests, programs, and features permanently. No recurring charges.
```

---

## 5. Pre-Launch Checklist

- [ ] App Store Connect: Create app record
- [ ] Upload build via Xcode (Product → Archive → Distribute)
- [ ] Add all 4 IAP products with descriptions
- [ ] Upload 5 screenshots for each required device size
- [ ] Fill in all metadata fields above
- [ ] Set pricing and availability (all regions)
- [ ] Add privacy nutrition labels (camera, health data)
- [ ] Submit for review
- [ ] Prepare social media launch posts (Day 1 content ready)
- [ ] Schedule Product Hunt launch for same week
- [ ] Send to 5-10 beta testers for initial reviews
