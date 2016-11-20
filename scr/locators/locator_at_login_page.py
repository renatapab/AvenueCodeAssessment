from selenium.webdriver.common.by import By


class Login(object):
    # A class for LOGIN page locators. All locators should come here
    EMAIL_TEXT_BOX = (By.ID, 'user_email')
    PWD_TEXT_BOX = (By.ID, 'user_password')
    LOGIN_BUTTON = (By.NAME, 'commit')

