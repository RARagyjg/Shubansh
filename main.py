from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75724784400%3AqUY6SK6h9qKLPT%3A8%3AAYcsh91FCzPoZvcRHwBAWW9heMpsxHh5n6B_NicyFg")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message reply templates (edit if you want)
reply_templates_master = [
    """𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓
𝚂𝚄𝙱𝙰𝙽𝚂𝙷^𝚃𝙴𝚁𝙸 𝙱𝙴𝙷𝙽 𝙺𝙸 𝙿𝙰𝙽𝚃𝚈 𝚄𝚃𝙰𝚁 𝙺𝙴 𝙱𝙾𝙾𝚁 𝙲𝙷𝙰𝚃𝚄𝙶𝙰________________________________________✓""",
"""𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/
𝐒𝐔𝐁𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐏𝐀𝐍𝐓𝐘 𝐅𝐀𝐃𝐔__________________________________________________/"""
]

# 🧠 Maintain last message replied for each user
last_msg_id_by_user = {}

def get_next_reply(username, history):
    # Filter replies jo already iss user ko bheje gaye ho
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    reply = random.choice(possible_replies)
    history.add(reply)
    return reply.replace("{user}", username)

user_reply_history = {}

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=1)

            for thread in threads:
                if not thread.messages:
                    continue

                latest_msg = thread.messages[0]

                # Apna msg ignore karo
                if latest_msg.user_id == me_id:
                    continue

                user_id = latest_msg.user_id
                username = cl.user_info(user_id).username

                # Agar same msg pe already reply kar chuke ho, skip karo
                if last_msg_id_by_user.get(user_id) == latest_msg.id:
                    continue

                # User history init if not exists
                if user_id not in user_reply_history:
                    user_reply_history[user_id] = set()

                # 📨 Generate new random reply
                reply = get_next_reply(username, user_reply_history[user_id])

                try:
                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(10, 20))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(10, 20))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(10, 20))

# 🚀 Start bot
auto_reply()
