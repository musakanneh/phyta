class OperatingSystem:
    multi_tasking = True
    name = "Windows System"


class Apple:
    website = "www.apple.com"
    name = "Apple MacBook Pro"


class MackBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multi_tasking == True:
            print("This is a multitasking system. Please visit {} for more details.".format(
                self.website))
            print("Name: {}".format(OperatingSystem.name))


mac_book = MackBook()
