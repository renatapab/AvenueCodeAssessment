# -*- coding: utf-8 -*-
import unittest
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from time import sleep
from selenium import webdriver
from scr.pages import page_login
from scr.pages import page_tasks
from scr.pages import page_navbar
from scr.pages import page_footbar
from scr.pages import page_home
from scr.pages import page_bug_tracker
from scr.pages import page_user_story



class CreateTask(unittest.TestCase):

    def setUp(self):
        # Headless
        # self.driver = webdriver.PhantomJS(executable_path=r"C:\PhantomJS\bin\phantomjs.exe")
        # With Head (Shows the Browser)
        # To show test running at chromes browsers, just remove the comments from these two next line
        # and comment the above line
        self.driver = webdriver.Chrome('C:/Projetos/configs/chromedriver_win32/chromedriver')
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(5)
        self.driver.get('http://qa-test.avenuecode.com/')

    def test_my_task_link_is_present_in_all_pages(self):
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        footbar = page_footbar.PageFoot(self.driver)
        home_page = page_home.PageHome(self.driver)
        bug_tracker_page = page_bug_tracker.PageBugTracker(self.driver)
        user_story_page = page_user_story.PageUserStory(self.driver)
        # Login
        print '\ntest_my_task_link_is_present_in_all_pages'
        # Login
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        sleep(1)

        # Check at Home page
        navbar.click_home_link()
        # Verify if it's in the right page
        self.assertIn('ToDo App', str(home_page.get_todo_app_head_title()))
        # check whether my task link is present at home page
        navbar.has_my_task_link()

        # Check at Bug Track page
        footbar.click_track_a_bug_link()
        # Verify if it's in the right page
        self.assertIn('Bugs I have found so far', str(bug_tracker_page.get_bug_head_title()))
        # check whether my task link is present at bug track page
        navbar.has_my_task_link()

        # Check at User Story page
        footbar.click_user_story_link()
        # Verify if it's in the right page
        self.assertIn('User Stories', str(user_story_page.get_todo_app_head_title()))
        # check whether my task link is present at user story page
        navbar.has_my_task_link()
        self.driver.close()
        print 'END'

    def test_my_task_link(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_adding_new_task_pressing_button'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        # Check at My Task page
        navbar.click_my_task_link()
        # Verify if it's in the right page
        self.assertIn('ToDo List', str(tasks_page.get_todo_list_head()))
        self.driver.close()
        print 'END'

    def test_adding_new_task_pressing_button(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_adding_new_task_pressing_button'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        sleep(1)
        # Verify whether its in the right page
        self.assertIn('ToDo List', str(tasks_page.get_todo_list_head()))
        # Add a new task
        tasks_page.add_a_task('Testing the add button')
        tasks_page.click_add_button()
        self.driver.close()
        print 'END'

    def test_adding_new_task_pressing_enter(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_adding_new_task_pressing_enter'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        # Verify whether its in the right page
        self.assertIn('ToDo List', str(tasks_page.get_todo_list_head()))
        # Add a new task
        tasks_page.add_a_task('Testing the return keyboard')
        tasks_page.press_enter_button()
        self.driver.close()
        print 'END'

    def test_welcome_message(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_adding_new_task_pressing_enter'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        self.assertEqual("renata's ToDo List", str(tasks_page.get_todo_list_head()))
        self.driver.close()
        print 'END'

    def test_ownership_message_at_the_top(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_ownership_message_at_the_top'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        # Verify if the head title is located at the top of the page
        self.assertLess(tasks_page.get_element_location_y(), 100)
        self.driver.close()
        print 'END'

    def test_add_3_char_to_task_name(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_add_3_char_to_task_name'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        tasks_page.add_a_task('qw')
        tasks_page.press_enter_button()
        # Checks if the new task is not present at the table
        self.assertFalse(tasks_page.first_task_has_element())
        self.driver.close()
        print 'END'

    def test_add_251_char_to_task_name(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_add_251_char_to_task_name'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        tasks_page.add_a_task('ieaiurhafsiduhfaidhfisahfiasuhfiuashdfiasuhdfiausfhiuashfiuahsfiuahsfiahsfipasnpfnjaskcnc'
                              'opnsOIJFOIJDSFOAIJSOFPIJASPOFJASOFIJASOIFJASOIJFAPOSJFD321321321315WE6R1QR1WQE65F16EW51C6'
                              'ASV1C6ASV61SV61A56V1A6FS1V6AF1V651D6V51A6S51V6A51V6D5F16V5A16V51A651F1V6F')
        tasks_page.press_enter_button()
        # Checks if the new task is not present at the table
        self.assertFalse(tasks_page.first_task_has_element())
        self.driver.close()
        print 'END'

    def test_a_valid_new_task_entrance_at_table_list(self):
        # Load pages
        login_page = page_login.PageLogin(self.driver)
        navbar = page_navbar.PageNavBar(self.driver)
        tasks_page = page_tasks.PageTasks(self.driver)
        # Login
        print '\ntest_a_valid_new_task_entrance_at_table_list'
        navbar.click_sign_in_link()
        login_page.type_email()
        login_page.type_password()
        login_page.click_login_button()
        navbar.click_my_task_link()
        tasks_page.add_a_task('Add a new task to check the table list')
        tasks_page.press_enter_button()
        # Checks if the new task is present at the table
        self.assertTrue(tasks_page.first_task_has_element())
        self.driver.close()
        print 'END'