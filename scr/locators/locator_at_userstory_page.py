from selenium.webdriver.common.by import By


class UserStoryPage(object):
    # A class for User Story page locators. All locators should come here
    USER_STORY_HEAD_LABEL = (By.TAG_NAME, 'h1')
