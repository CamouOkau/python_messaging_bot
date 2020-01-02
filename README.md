# messenger_new_years_bot
A messenger bot that messages the people you care about on new year's.


# Getting started
## prerequisites:
To be able to run this code you have to have install all listed packages in *requirements.txt*.
  
## installation:
Simply git pull this repo.

# User guide
## What and how do I run this?
It's easy! If you have followed all the steps in **Getting started**, you need to:
1. Input all the usernames in *users.txt* you want the bot to send messages to.
2. If you want to change the message, modify *message.txt* to your liking, all the text will be sent.
2. Run *send.py*: `python3.6 send.py <your email> <your password>
  > Careful! Replace `<your email>` and `<your password>` with your **actuall** messenger *email* and *password*.
3. You're done! The messages will be sent to your friends at excatly 00:00 new year's eve (local time).
> Also, you have to let the program run until 00:00 or else it won't send the messages. At 00:00 it should terminate by itself.
