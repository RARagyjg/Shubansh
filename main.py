from instagrapi import Client
import time
import random
import itertools
from flask import Flask

# ================= SETTINGS =================
SESSION_ID = "75694570387%3ALD2zAKHLoWKc17%3A18%3AAYihO7CIDRmV7AV0T_DKUwMyFcTCCdHdchkL6HTq8w"
GROUP_THREAD_ID = "2859303934258963"
# ============================================

# Flask keep-alive
app = Flask(__name__)

@app.route("/")
def home():
    return "INSTAGRAM SPAM BOT RUNNING 24/7 🔥"

# Instagram Client Login
cl = Client()
cl.login_by_sessionid(SESSION_ID)

# Message list
reply_templates = [
   """Oᗰᗩ ᘜᗩᖇᗴᗴᗷ - TERI MA KE SATH SEX AKRAOGA AGAR BHAGA TO BHIKARI _____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ Oᗰᗩ ᘜᗩᖇᗴᗴᗷ - RANDI TERI MAAA MERE LODE PAR"""
]

# Infinite message cycle
msg_cycle = itertools.cycle(reply_templates)

def start_gc_autospam():
    print(f"🚀 Spamming started in GC: {GROUP_THREAD_ID}")

    while True:
        try:
            msg = next(msg_cycle)
            cl.direct_answer(GROUP_THREAD_ID, msg)

            print(f"✔️ Sent: {msg}")

            # SAFE DELAY (30–60 sec)
            time.sleep(random.randint(40, 60))

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# Run spam bot in background thread
import threading
threading.Thread(target=start_gc_autospam).start()

# Start Flask server (keeps Render alive)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
