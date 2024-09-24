# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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
