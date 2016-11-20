from scr.localActions import local_web_elements
from scr.locators import locator_at_userstory_page


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageUserStory(BasePage):
    def get_todo_app_head_title(self):
        return local_web_elements.MyWebElement(self.driver).\
            get_result(locator_at_userstory_page.UserStoryPage.USER_STORY_HEAD_LABEL, 'get_todo_app_head_title')

    def click_track_a_bug_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_footbar.FootBar.BUG_TRACKER_LINK, 'click_track_a_bug_link')