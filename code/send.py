import sys
import time
from datetime import datetime
from bot import MessengerBot


if __name__ == "__main__":
    try:
        email = sys.argv[1]
        password = sys.argv[2]

        bot = MessengerBot(email, password)

        with open("users.txt", "r") as file:
            users = dict.fromkeys(file.read().split("\n"))

            for user in users:
                users[user] = bot.uid(user)

        with open("message.txt", "r") as file:
            message = file.read()
        
        time_now = datetime.now()
        send_time = datetime(time_now.year + 1, 1, 1)

        wait_time = (send_time - time_now).total_seconds()
        
        print("Waiting...")
        time.sleep(wait_time)

        for uid in users.values():
            bot.send_message(message, uid)

        bot.logout()

    except IndexError:
            print("No email or password")
