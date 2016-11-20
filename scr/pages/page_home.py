from scr.localActions import local_web_elements
from scr.locators import locator_at_home_page


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageHome(BasePage):
    def get_todo_app_head_title(self):
        return local_web_elements.MyWebElement(self.driver).get_result(locator_at_home_page.Home.TO_DO_APP_HEAD, 'get_todo_app_head_title')