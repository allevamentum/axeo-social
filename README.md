# axeo-social

Content management and automation pipeline for Axeo social media marketing.

## Structure

```
axeo-social/
├── content/
│   ├── week-01/          # Week 1 content (49 posts)
│   │   ├── monday.json
│   │   ├── tuesday.json
│   │   └── ...
│   └── templates/
│       ├── hooks.md      # Reusable hook library
│       ├── ctas.md       # Call-to-action library
│       └── hashtags.md   # Hashtag strategy
├── assets/
│   ├── CANVA_TEMPLATES.md  # Design specs for Canva
│   ├── thumbnails/
│   ├── carousels/
│   └── videos/
├── analytics/
│   └── weekly-report-template.md
├── scripts/
│   ├── generate-captions.py  # Claude API content gen
│   └── post-to-buffer.py     # Buffer API scheduling
├── profiles/
│   └── SETUP_GUIDE.md        # Account setup for all platforms
└── APP_STORE_SUBMISSION.md    # App Store metadata & checklist
```

## Quick Start

### 1. Generate content for a week
```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key
python scripts/generate-captions.py --week 2
```

### 2. Schedule via Buffer
```bash
pip install requests
export BUFFER_ACCESS_TOKEN=your_token
python scripts/post-to-buffer.py --week 1 --list-profiles
python scripts/post-to-buffer.py --week 1
```

### 3. Weekly workflow
1. Sunday: Run `generate-captions.py` for next week
2. Review and edit generated content
3. Create visuals in Canva using templates
4. Schedule via Buffer + Meta Business Suite
5. Friday: Fill in weekly analytics report

## Links

- Website: https://axeo.vision
- iOS App: App Store (pending review)
- Strategy: See AXEO_MARKETING_STRATEGY.md in parent directory
