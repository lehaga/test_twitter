import unittest
from testconfig import TestConfig
from selenium import webdriver
from pages.login_page import LoginPage


class LoginPageTests(unittest.TestCase):

    MESSAGE = 'The email and password you entered did not match our records. Please double-check and try again.'

    def setUp(self):
        self.config = TestConfig()
        self.webdriver = webdriver.Firefox()
        self.webdriver.get(self.config.url)
        self.test_user = self.config.user
        self.test_password = self.config.password

    def tearDown(self):
        self.webdriver.quit()

    def test_login_page(self):
        login_page = LoginPage(self.webdriver)
        login_page.is_login_page()
        login_page.set_user(self.test_user)
        login_page.set_password(self.test_password)
        login_page.log_in()

    def test_no_password(self):
        login_page = LoginPage(self.webdriver)
        login_page.is_login_page()
        login_page.set_user(self.test_user)
        login_page.click_login_button()
        self.assertTrue(login_page.has_error(self.MESSAGE), 'Wrong error message displayed')

    def test_no_user(self):
        login_page = LoginPage(self.webdriver)
        login_page.is_login_page()
        login_page.set_password(self.test_password)
        login_page.click_login_button()
        self.assertTrue(login_page.has_error(self.MESSAGE), 'Wrong error message displayed')

    def test_no_user_or_password(self):
        login_page = LoginPage(self.webdriver)
        login_page.is_login_page()
        login_page.click_login_button()
        self.assertTrue(login_page.has_error(self.MESSAGE), 'Wrong error message displayed')






