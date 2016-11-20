from lettuce import world

from scr.localActions import local_web_elements
from scr.locators import locator_at_subtasks


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageSubTasks(BasePage):
    def get_placeholder_attribute(self):
        return local_web_elements.MyWebElement(self.driver).get_placeholder_attribute(locator_at_subtasks.SubTasks.DUE_DATE_FIELD, 'get_placeholder_attribute')