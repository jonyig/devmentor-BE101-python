from language import Language


class Zhtw(Language):
    def __init__(self):
        self.msg = {
            "signup": "註冊成功",
            "subscribe": "訂閱成功",
            "cancel": "取消成功"
        }

    def get_msg(self, msg_key: str) -> str:
        return self.msg[msg_key]
