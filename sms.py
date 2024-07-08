from route import Route
class Sms(Route):
    def send(self,msg):
        print(f"Sending message on SMS: {msg}")