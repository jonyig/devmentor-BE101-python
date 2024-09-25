# UserEventManager manage user's event
from user import User
from eventhandler import EventHandler


class UserEventManager:
    def __init__(self, user: User):
        self.user = user

    def user_register(self):
        event = self.user.register()
        event_handler = EventHandler(event,self.user)
        register_event = event_handler.handle_event()
        register_event.notify()

    def book_course(self):
        event = self.user.course_booking()
        event_handler = EventHandler(event,self.user)
        book_course_event = event_handler.handle_event()
        book_course_event.notify()

    def cancel_course(self):
        event = self.user.course_cancel()
        event_handler = EventHandler(event,self.user)
        cancel_course_event = event_handler.handle_event()
        cancel_course_event.notify()