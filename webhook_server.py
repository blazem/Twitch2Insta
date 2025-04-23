from flask import Flask, request
import subprocess
import threading

app = Flask(__name__)

@app.route("/trigger", methods=["GET"])
def trigger():
    threading.Thread(target=handle_trigger).start()
    return "Triggered!", 200

def handle_trigger():
    subprocess.call(["python3", "snapshot.py"])
    subprocess.call(["python3", "post_instagram.py"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
