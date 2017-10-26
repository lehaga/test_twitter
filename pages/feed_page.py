from pages.PageObject import PageObject
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as expected_conditions
from selenium.webdriver.common.by import By


class FeedPage(PageObject):
    """ Time to wait for the page to load """
    TIME_TO_WAIT = 15

    class Locators(object):
        EXAMPLE_LOCATOR = (By.XPATH, "")

    def wait_for_page(self):
        """ Wait for the page to load """
        WebDriverWait(self.webdriver, self.TIME_TO_WAIT)\
            .until(expected_conditions.visibility_of_element_located(self.Locators.EXAMPLE_LOCATOR))