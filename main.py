from instagrapi import Client
import time
import random
import itertools

# ========== SETTINGS ==========
SESSION_ID = "75694570387%3ALD2zAKHLoWKc17%3A18%3AAYihO7CIDRmV7AV0T_DKUwMyFcTCCdHdchkL6HTq8w"
GROUP_THREAD_ID = "2859303934258963"
# ===============================

cl = Client()
cl.login_by_sessionid(SESSION_ID)

# Message list
reply_templates = [
    """OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂OMA KI MA RNDI 😂""",
    """BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋BLACK KI MA RNDI💋 """,
    """SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗SAM KI MA RNDI💗"""
]

# Infinite cycle
msg_cycle = itertools.cycle(reply_templates)

def start_gc_autospam():
    print(f"🚀 Spamming started in GC: {GROUP_THREAD_ID}")

    while True:
        try:
            msg = next(msg_cycle)
            cl.direct_answer(GROUP_THREAD_ID, msg)

            print(f"✔️ Sent: {msg}")

            # safe delay
            time.sleep(random.randint(30, 60))

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

start_gc_autospam()
