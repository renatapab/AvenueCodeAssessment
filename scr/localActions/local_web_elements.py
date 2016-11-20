# -*- coding: utf-8 -*-
from lettuce import world
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from scr.localActions import local_messages


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MyWebElement(BasePage):
    def click(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            element.click()
            print(element_description + ' ' + local_messages.executed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def click_drop_box(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            self.driver.execute_script("$(arguments[0]).click();", element)
            print(element_description + ' ' + local_messages.executed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))

    def has_element(self, selector):
        try:
            self.driver.find_element(*selector)
            return True
        except NoSuchElementException:
            print('Element does not exist')
            return False

    def is_element_enabled(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            is_enable = element.is_enabled()
            print(element_description + ' ' + local_messages.button_enable + str(is_enable))
            return is_enable
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))

    def login_as(self, selector, login, element_description):
        try:
            element = self.driver.find_element(*selector)
            element.send_keys(login)
            print(element_description + ' ' + local_messages.executed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))

    def select_option_by_value(self, selector, value, element_description):
        try:
            element = Select(self.driver.find_element(*selector))
            element.select_by_value(value)
            print(element_description + ' ' + local_messages.executed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def get_result(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            value = element.text
            print(element_description + ' ' + local_messages.executed)
            return value
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def set_text(self, selector, text, element_description):
        try:
            element = self.driver.find_element(*selector)
            element.send_keys(text)
            print(element_description + ' ' + local_messages.informed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def press_enter(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            element.send_keys(Keys.RETURN)
            print(element_description + ' ' + local_messages.executed)
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def get_location_y(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            value = element.location['y']
            print element_description + ' ' + local_messages.executed
            return value
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()

    def get_location_x(self, selector, element_description):
        try:
            element = self.driver.find_element(*selector)
            value = element.location['x']
            print element_description + ' ' + local_messages.executed
            return value
        except NoSuchElementException as e:
            print(local_messages.exception_message + ('%s' % e))
            self.driver.quit()
