from selenium.webdriver.common.by import By


class NavBar(object):
    # A class for NavBar locators. All locators should come here
    MY_TASK_LINK = (By.LINK_TEXT, 'My Tasks')
    SIGN_IN_LINK = (By.LINK_TEXT, 'Sign In')
    HOME_LINK = (By.LINK_TEXT, 'Home')
