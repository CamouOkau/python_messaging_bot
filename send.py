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

        message = "Happy new year's!"
        send_time = datetime(2021, 1, 1)

        wait_time = (send_time - datetime.now()).total_seconds()
        time.sleep(wait_time)

        for user in users:
            uid = bot.uid(user)
            bot.send_message(message, uid)

        bot.logout()

    except IndexError:
            print("No email or password")