from instagrapi import Client
from datetime import datetime
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD

cl = Client()
try:
    cl.load_settings("ig_settings.json")
except:
    pass

if not cl.user_id:
    cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    cl.dump_settings("ig_settings.json")

caption = f"Live now on Twitch! Snapshot at {datetime.now().strftime('%H:%M %d-%m-%Y')}"
cl.photo_upload("stream_snapshot.jpg", caption)
