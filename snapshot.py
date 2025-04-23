import subprocess

from config import TWITCH_CHANNEL

twitch_url = f"https://twitch.tv/{TWITCH_CHANNEL}"
output_file = "stream_snapshot.jpg"

stream_url = subprocess.check_output(["streamlink", "--stream-url", twitch_url, "best"]).decode().strip()

subprocess.call([
    "ffmpeg", "-y", "-i", stream_url, "-frames:v", "1", "-q:v", "2", output_file
])
