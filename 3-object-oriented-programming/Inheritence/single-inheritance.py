class Apple:
    """"""
    manufacturer = "Apple Inc"
    contact_website = "www.apple.com"

    def contact_details(self):
        print("To contact us, visit: {}".format(self.contact_website))


class MacBook(Apple):
    """A derived class inheriting from the Apple (base)
    class

    """

    def __init__(self):
        self.manifacture_year = 2017

    def manufacturer_details(self):
        """Prints the MacBook's details"""
        print("This PC was manifactired in the year {} by {}".format(
            self.manifacture_year, self.manufacturer))


mac_book = MacBook()
mac_book.manufacturer_details()
mac_book.contact_details()
