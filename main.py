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

# Event Interface
class Event(ABC):
    @abstractmethod
    def add_channel(self, notification: Notification):
        """
        Every event should have an add_channel method
        """
        pass

    @abstractmethod
    def notify(self, user: User):
        """
        Every event should have a notify method
        """
        pass


# RegisterEvent
class RegisterEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "註冊成功", "en-US": "Registration Successful"}
        self.channels = [Email(), SMS()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Registration Successful")
        for channel in self.channels:
            channel.send_message(message, user)


# CourseBookingEvent
class CourseBookingEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "學生預約課程成功", "en-US": "Course Booking Successful"}
        self.channels = [Email(), Telegram()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Course Booking Successful")
        for channel in self.channels:
            channel.send_message(message, user)


# CourseCancelEvent
class CourseCancelEvent(Event):
    def __init__(self):
        self.content = {"zh-TW": "學生取消課程", "en-US": "Course Cancellation"}
        self.channels = [Email(), Telegram()]

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self, user: User):
        message = self.content.get(user.prefers_language, "Course Cancellation")
        for channel in self.channels:
            channel.send_message(message, user)

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
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi123456, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
