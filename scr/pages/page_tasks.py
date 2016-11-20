from lettuce import world

from scr.localActions import local_web_elements
from scr.locators import locator_at_tasks_page


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageTasks(BasePage):
    def has_task_list_table(self):
        return local_web_elements.MyWebElement(self.driver).has_element(locator_at_tasks_page.Tasks.TO_BE_DONE_TABLE_HEAD)

    def get_todo_list_head(self):
        return local_web_elements.MyWebElement(self.driver).get_result(locator_at_tasks_page.Tasks.TO_DO_HEAD_LABEL, 'get_todo_list_head')

    def add_a_task(self, task):
        return local_web_elements.MyWebElement(self.driver).set_text(locator_at_tasks_page.Tasks.NEW_TASK_FORM, task, 'add_a_task')

    def click_add_button(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_tasks_page.Tasks.ADD_BUTTON, 'click_add_button')

    def press_enter_button(self):
        return local_web_elements.MyWebElement(self.driver).press_enter(locator_at_tasks_page.Tasks.NEW_TASK_FORM, 'press_enter_button')

    def get_element_location_y(self):
        return local_web_elements.MyWebElement(self.driver).get_location_y(locator_at_tasks_page.Tasks.TO_DO_HEAD_LABEL, 'get_element_location_y')

    def first_task_has_element(self):
        return local_web_elements.MyWebElement(self.driver).has_element(locator_at_tasks_page.Tasks.FIRST_TASK_ON_THE_LIST_LINK_TEXT)
