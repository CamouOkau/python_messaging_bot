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

        time_now = datetime.now()
        send_time = datetime(time_now.year + 1, 1, 1)

        with open("message.txt", "r") as file:
            message = file.read()

        wait_time = (send_time - time_now).total_seconds()
        time.sleep(wait_time)

        for user in users:
            uid = bot.uid(user)
            bot.send_message(message, uid)

        bot.logout()

    except IndexError:
            print("No email or password")
