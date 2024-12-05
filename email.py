from route import Route
class Email(Route):
    def send(self,msg):
        print(f"Sending message on Email: {msg}")