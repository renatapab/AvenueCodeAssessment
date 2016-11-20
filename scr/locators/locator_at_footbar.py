from selenium.webdriver.common.by import By


class FootBar(object):
    # A class for Foot bar locators. All main page locators should come here
    BUG_TRACKER_LINK = (By.LINK_TEXT, 'Track a Bug')
    TEST_DESCRIPTION_LINK = (By.LINK_TEXT, 'Test Description - User Stories')
