
# UserEventManager manage user's event
class UserEventManager:
    def __init__(self, user: User):
        self.user = user

    def user_register(self):
        register_event = self.user.register()
        register_event.notify(self.user)

    def book_course(self):
        booking_event = self.user.course_booking()
        booking_event.notify(self.user)

    def cancel_course(self):
        cancel_event = self.user.course_cancel()
        cancel_event.notify(self.user)