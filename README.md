# Python messaging bot
A messaging bot written in python, that can automatically send messages to
multiple users at a predetermined time. Currently, only messaging
through facebook is supported, but in the future I plan on adding sms
support.

## User guide
1. Install all the listed packages in *requirements.txt*.
 > pip install -r requirements.txt
2. Navigate yourself to the *code* directory.
 > cd code
3. Input all the users you want to send the message to in *users.txt*.
4. Modify *message.txt* to your liking. This is the text that will be sent.
5. Run *send*.py*: `python send.py <your email> <your password>`
  > Replace `<your email>` and `<your password>` with your **actual** messenger *email* and *password*.
6. You're done! The messages will be sent to your friends at excatly 00:00 new year's eve (local time).
  > The program will terminate itself after sending out the messages.
