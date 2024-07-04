from language import Language


class Enus(Language):
    def __init__(self):
        self.msg = {
            "signup": "signed up SUCCESSFULLY",
            "subscribe": "subscribed SUCCESSFULLY",
            "cancel": "cancelled SUCCESSFULLY"
        }

    def get_msg(self, msg_key: str) -> str:
        return self.msg[msg_key]