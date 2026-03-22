#!/usr/bin/env python3
"""
AXEO Buffer Scheduler
Reads weekly content JSON and schedules posts via Buffer API.

Requirements: pip install requests
Set BUFFER_ACCESS_TOKEN environment variable.
Get token: https://buffer.com/developers/api

Usage:
  python post-to-buffer.py --week 1 --day monday
  python post-to-buffer.py --week 1  # schedules entire week
"""

import json
import os
import requests
import argparse
from datetime import datetime, timedelta

BUFFER_API = "https://api.bufferapp.com/1"
TOKEN = os.getenv("BUFFER_ACCESS_TOKEN")

# Map platform names to Buffer profile IDs
# Fill these in after connecting accounts in Buffer
PROFILE_IDS = {
    "tiktok": os.getenv("BUFFER_TIKTOK_ID", ""),
    "x": os.getenv("BUFFER_X_ID", ""),
    "linkedin": os.getenv("BUFFER_LINKEDIN_ID", ""),
}

SUPPORTED_PLATFORMS = set(PROFILE_IDS.keys())


def get_profiles():
    """List all connected Buffer profiles."""
    r = requests.get(f"{BUFFER_API}/profiles.json", params={"access_token": TOKEN})
    r.raise_for_status()
    for p in r.json():
        print(f"  {p['service']}: {p['id']} — @{p.get('service_username', 'N/A')}")
    return r.json()


def schedule_post(profile_id: str, text: str, scheduled_at: str = None, media_link: str = None):
    """Schedule a single post to Buffer."""
    data = {
        "access_token": TOKEN,
        "profile_ids[]": profile_id,
        "text": text,
        "now": scheduled_at is None,
    }

    if scheduled_at:
        data["scheduled_at"] = scheduled_at

    if media_link:
        data["media[link]"] = media_link

    r = requests.post(f"{BUFFER_API}/updates/create.json", data=data)
    r.raise_for_status()
    return r.json()


def load_day_content(week: int, day: str) -> list:
    """Load posts from a day's JSON file."""
    filepath = f"content/week-{week:02d}/{day}.json"
    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return []
    with open(filepath) as f:
        data = json.load(f)
    return data.get("posts", [])


def schedule_day(week: int, day: str, base_date: datetime):
    """Schedule all Buffer-compatible posts for a day."""
    posts = load_day_content(week, day)

    scheduled = 0
    skipped = 0

    for post in posts:
        platform = post.get("platform", "")

        # Only schedule platforms connected to Buffer
        if platform not in SUPPORTED_PLATFORMS:
            skipped += 1
            continue

        profile_id = PROFILE_IDS.get(platform)
        if not profile_id:
            print(f"  No Buffer profile ID for {platform} — skipping")
            skipped += 1
            continue

        # Parse time from post
        time_str = post.get("time", "12:00")
        hour, minute = map(int, time_str.split(":"))
        scheduled_at = base_date.replace(hour=hour, minute=minute)

        caption = post.get("caption", "")
        cta = post.get("cta", "")
        text = f"{caption}\n\n{cta}" if cta else caption

        try:
            result = schedule_post(
                profile_id=profile_id,
                text=text,
                scheduled_at=scheduled_at.isoformat()
            )
            print(f"  Scheduled: [{platform}] {post.get('hook', '')[:50]}...")
            scheduled += 1
        except Exception as e:
            print(f"  Error scheduling [{platform}]: {e}")

    print(f"  Day total: {scheduled} scheduled, {skipped} skipped (other platforms)")


def main():
    parser = argparse.ArgumentParser(description='Schedule Axeo content via Buffer')
    parser.add_argument('--week', type=int, required=True, help='Week number')
    parser.add_argument('--day', type=str, default=None, help='Specific day (monday-sunday)')
    parser.add_argument('--list-profiles', action='store_true', help='List Buffer profiles')
    parser.add_argument('--start-date', type=str, default=None,
                       help='Start date for the week (YYYY-MM-DD). Default: next Monday.')
    args = parser.parse_args()

    if not TOKEN:
        print("Error: Set BUFFER_ACCESS_TOKEN environment variable")
        print("Get your token at: https://buffer.com/developers/api")
        return

    if args.list_profiles:
        print("Connected Buffer profiles:")
        get_profiles()
        return

    # Calculate base date
    if args.start_date:
        base = datetime.strptime(args.start_date, "%Y-%m-%d")
    else:
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        base = today + timedelta(days=days_until_monday)

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    if args.day:
        if args.day.lower() not in days:
            print(f"Invalid day: {args.day}")
            return
        day_offset = days.index(args.day.lower())
        date = base + timedelta(days=day_offset)
        print(f"\nScheduling {args.day.capitalize()} (Week {args.week}) — {date.strftime('%B %d')}")
        schedule_day(args.week, args.day.lower(), date)
    else:
        print(f"\nScheduling full Week {args.week} starting {base.strftime('%B %d, %Y')}")
        for i, day in enumerate(days):
            date = base + timedelta(days=i)
            print(f"\n{day.upper()} — {date.strftime('%B %d')}")
            schedule_day(args.week, day, date)


if __name__ == "__main__":
    main()
