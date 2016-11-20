from scr.localActions import local_web_elements
from scr.localActions import local_logins
from scr.locators import locator_at_login_page


class BasePage (object):

    def __init__(self, driver):
        self.driver = driver


class PageLogin(BasePage):
    def type_email(self):
        return local_web_elements.MyWebElement(self.driver).set_text(locator_at_login_page.Login.EMAIL_TEXT_BOX,
                                                                     local_logins.login, 'type_email')

    def type_password(self):
        return local_web_elements.MyWebElement(self.driver).set_text(locator_at_login_page.Login.PWD_TEXT_BOX,
                                                                     local_logins.pwd, 'type_password')

    def click_login_button(self):
        return local_web_elements.MyWebElement(self.driver).click(locator_at_login_page.Login.LOGIN_BUTTON, 'login')
