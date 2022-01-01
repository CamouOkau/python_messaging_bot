from fbchat import Client
from fbchat.models import Message as fb_message


class FbMessengerBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.client = Client(email, password)

    def get_uid(self, username):
        try:
            user = self.client.searchForUsers(username)[0]
            return user.uid
        except IndexError:
            print(f"User \"{username}\" does not exist!")

    def send_message(self, message, uid):
        if type(uid) is None:
            print(f"Uid \"{uid}\" does not exist!")
        else:
            self.client.send(fb_message(message), uid)

    def logout(self):
        self.client.logout()
