# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod

# Notification Interface
class Notification(ABC):

    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        """
        Every notification should have a send_message method
        """
        pass
# Email Notification
class Email(Notification):
    def send_message(self, message: str, user: 'User'):
        print(f"Sending Email to {user.email}: {message}")
# SMS Notification
class SMS(Notification):
    def send_message(self, message: str, user: 'User'):
        print(f"Sending SMS to {user.phone}: {message}")

# Telegram Notification
class Telegram(Notification):
    def send_message(self, message: str, user: 'User'):
        print(f"Sending Telegram message to {user.id}: {message}")
# User class
class User:
    def __init__(self, id: str, email: str, phone: str, prefers_language: str):
        self.id = id
        self.email = email
        self.phone = phone
        self.prefers_language = prefers_language

    def register(self):
        return RegisterEvent()

    def course_booking(self):
        return CourseBookingEvent()

    def course_cancel(self):
        return CourseCancelEvent()


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
def main(name):
    # create user
    user = User(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")

    # create UserEventManager
    user_event_manager = UserEventManager(user)

    # execute register operation
    user_event_manager.user_register()

    # execute book course operation
    user_event_manager.book_course()

    # execute cancel course operation
    user_event_manager.cancel_course()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
