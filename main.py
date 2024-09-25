# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from user import User
from eventmanager import UserEventManager


def main():
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
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
