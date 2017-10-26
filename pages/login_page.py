from selenium.webdriver.common.by import By

from pages.PageObject import PageObject
from pages.feed_page import FeedPage


class LoginPage(PageObject):

    class Locators(object):
        """ A collection of tuples used to locate UI elements. """
        LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'submit')]")
        USER_TEXT = (By.XPATH, "//*[contains(@name,'email') and contains(@class,'focus')]")
        PASSWORD_TEXT = (By.XPATH, "//*[contains(@class,'password-field')]")
        STATUS_LABEL = (By.XPATH, "//*[contains(@class,'message-text')]")

    def is_login_page(self):
        return self.webdriver.title == 'Login on Twitter'

    def log_in(self):
        """ Clicks the login button and waits for arrival at the Feed page. """
        self.click_login_button()
        feed_page = FeedPage(self.webdriver)
        feed_page.wait_for_page()
        return feed_page

    def click_login_button(self):
        self.webdriver.find_element(self.Locators.LOGIN_BUTTON).click()

    def set_user(self, user):
        self.webdriver.find_element(self.Locators.USER_TEXT).send_keys(user)

    def set_password(self, password):
        self.webdriver.find_element(self.Locators.PASSWORD_TEXT).send_keys(password)

    def has_error(self, message):
        return str(self.webdriver.find_element(self.Locators.STATUS_LABEL).text).strip() == message


