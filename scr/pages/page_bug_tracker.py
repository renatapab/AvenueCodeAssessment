from scr.localActions import local_web_elements
from scr.locators import locator_at_bug_tracker_page


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageBugTracker(BasePage):
    def get_bug_head_title(self):
        return local_web_elements.MyWebElement(self.driver).get_result(locator_at_bug_tracker_page.BugTracker.BUG_TRACKER_HEAD_TITLE, 'get_bug_head_title')
