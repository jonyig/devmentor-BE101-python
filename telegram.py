from route import Route
class Telegram(Route):
    def send(self,msg):
        print(f"Sending message on Telegram: {msg}")