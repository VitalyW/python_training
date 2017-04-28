from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.binary = FirefoxBinary("/Users/vitaly/Documents/Firefox_esr_45/Firefox.app/Contents/MacOS/firefox")
        self.wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary=self.binary)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()