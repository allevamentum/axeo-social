#!/usr/bin/env python3
"""
AXEO Social Content Generator
Uses Claude API to generate weekly content batches.

Requirements: pip install anthropic
Set ANTHROPIC_API_KEY environment variable.
"""

import anthropic
import json
import os
from datetime import datetime, timedelta

SYSTEM_PROMPT = """You are the social media manager for Axeo, an eye training app.

Brand details:
- App: Axeo — science-backed eye training
- Website: axeo.vision
- Free exercises: axeo.vision/exercise (6 free, 17 total)
- Free vision tests: axeo.vision/test (Snellen + Ishihara)
- iOS app with ARKit eye tracking
- Pricing: $2.99/wk, $5.99/mo, $34.99/yr, $89.99 lifetime
- 3 programs: Digital Eye Relief (30 days), Vision After 40 (45 days), Dry Eye Relief (30 days)
- Based on AAO & COVD clinical guidelines
- Brand voice: Clinical authority + accessible warmth. Never clickbait. Always backed by data.

Content pillars (% allocation):
1. Shock & Awe (30%) — Scroll-stopping stats, surprising facts
2. Education (25%) — Tips, how-tos, myth-busting
3. Demo & Proof (20%) — App demos, before/after, exercise walkthroughs
4. Community (15%) — UGC, challenges, polls, engagement bait
5. Conversion (10%) — Pricing, features, trials, App Store CTA

Always include:
- A hook in the first line (stop the scroll)
- Platform-native tone
- 3-5 relevant hashtags for TikTok/Instagram
- A clear CTA
"""

def generate_weekly_content(week_number: int) -> dict:
    client = anthropic.Anthropic()

    start_date = datetime.now() + timedelta(weeks=week_number - 1)

    prompt = f"""Generate a complete week of social media content for Week {week_number}.
    Starting date: {start_date.strftime('%B %d, %Y')}

    Create 7 posts per day (49 total) following this distribution:
    - TikTok: 2/day (AM and PM)
    - Instagram: 1 Reel + 1 Story per day
    - YouTube Shorts: 1/day
    - X (Twitter): 2/day
    - Reddit: 3 posts total (Wed, Sat, Sun) — replace one X post
    - LinkedIn: 2 posts total (Thu, Fri) — replace one X post

    For each post, provide:
    - platform
    - time (suggested posting time)
    - pillar (shock/education/demo/community/conversion)
    - hook (first line that stops the scroll)
    - caption (full post text, platform-native)
    - visual_notes (what to film/design)
    - cta (call to action)

    Return as JSON with this structure:
    {{
      "week": {week_number},
      "days": {{
        "monday": [{{...posts}}],
        "tuesday": [{{...posts}}],
        ...
      }}
    }}

    Make content fresh and non-repetitive. Reference current trends where possible.
    """

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    # Parse response
    content = message.content[0].text

    # Try to extract JSON from response
    try:
        # Find JSON block in response
        start = content.index('{')
        end = content.rindex('}') + 1
        return json.loads(content[start:end])
    except (ValueError, json.JSONDecodeError):
        return {"raw": content}


def save_content(week_data: dict, week_number: int):
    week_dir = f"content/week-{week_number:02d}"
    os.makedirs(week_dir, exist_ok=True)

    if "days" in week_data:
        for day, posts in week_data["days"].items():
            filepath = os.path.join(week_dir, f"{day}.json")
            with open(filepath, 'w') as f:
                json.dump({"day": day, "week": week_number, "posts": posts}, f, indent=2)
            print(f"  Saved {filepath} ({len(posts)} posts)")
    else:
        filepath = os.path.join(week_dir, "raw_output.json")
        with open(filepath, 'w') as f:
            json.dump(week_data, f, indent=2)
        print(f"  Saved raw output to {filepath}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate Axeo social media content')
    parser.add_argument('--week', type=int, default=1, help='Week number to generate')
    parser.add_argument('--weeks', type=int, default=1, help='Number of weeks to generate')
    args = parser.parse_args()

    for w in range(args.week, args.week + args.weeks):
        print(f"\nGenerating Week {w}...")
        content = generate_weekly_content(w)
        save_content(content, w)
        print(f"Week {w} complete!")


if __name__ == "__main__":
    main()
