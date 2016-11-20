from scr.localActions import local_web_elements
from scr.locators import locator_at_footbar


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageFoot(BasePage):
    def click_track_a_bug_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_footbar.FootBar.BUG_TRACKER_LINK, 'click_track_a_bug_link')

    def click_user_story_link(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_footbar.FootBar.TEST_DESCRIPTION_LINK, 'click_user_story_link')

    def get_bug_head_title(self):
        return local_web_elements.MyWebElement(self.driver).get_result(locator_at_footbar.FootBar.BUG_TRACKER_LINK, 'def get_bug_head_title')

    def has_bug_track_link(self):
        return local_web_elements.MyWebElement(self.driver).has_element(locator_at_footbar.FootBar.BUG_TRACKER_LINK)
