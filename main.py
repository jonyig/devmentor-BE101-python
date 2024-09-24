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




def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi123456, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
