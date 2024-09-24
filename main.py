# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi123456, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
