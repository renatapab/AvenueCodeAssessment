from scr.localActions import local_web_elements
from scr.locators import locator_at_navbar


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageNavBar(BasePage):
    def click_sign_in_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_navbar.NavBar.SIGN_IN_LINK, 'click_sign_in_link')

    def has_my_task_link(self):
        return local_web_elements.MyWebElement(self.driver).has_element(locator_at_navbar.NavBar.MY_TASK_LINK)

    def click_my_task_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_navbar.NavBar.MY_TASK_LINK, 'click_my_task_link')

    def click_home_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_navbar.NavBar.HOME_LINK, 'click_home_link')