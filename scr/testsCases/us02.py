# -*- coding: utf-8 -*-
import unittest
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium import webdriver
from scr.pages import page_login
from scr.pages import page_tasks
from scr.pages import page_navbar
from scr.pages import page_subtask



class CreateSubTask(unittest.TestCase):

    def setUp(self):
        # Headless
        # self.driver = webdriver.PhantomJS(executable_path=r"C:\Projetos\configs\PhantomJS\bin\phantomjs.exe")
        # With Head (Shows the Browser)
        # To show test running at chromes browsers, just remove the comments from these two next line
        # and comment the above line
        self.driver = webdriver.Chrome('C:/Projetos/configs/chromedriver_win32/chromedriver')
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(5)
        self.driver.get('http://qa-test.avenuecode.com/')

    def test_is_enable_manage_subtask_button(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_is_enable_manage_subtask_button'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        tasks_page.add_a_task('Add a new task to check manager subtask button')
        tasks_page.press_enter_button()
        # Checks if the new task is present at the table
        self.assertTrue(tasks_page.manager_subtask_button_is_enable())
        self.driver.close()
        print 'END'

    def test_subtasks_quantity_at_button(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_is_enable_manage_subtask_button'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        # Checks if subtask quantity is present at the manage subtask button
        self.assertRegexpMatches(tasks_page.get_number_of_subtask_at_button(), '0')
        self.driver.close()
        print 'END'

    def test_subtask_due_date_format(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        subtask_page = page_subtask.PageSubTasks(self.driver)
        # Login
        print '\ntest_is_enable_manage_subtask_button'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        tasks_page.click_manage_subtask_button()
        # Checks if due date is following MM/dd/yyyy format
        self.assertEqual(subtask_page.get_placeholder_attribute(), 'MM/dd/yyyy')
        self.driver.close()
        print 'END'

    def tearDown(self):
        self.driver.quit()
