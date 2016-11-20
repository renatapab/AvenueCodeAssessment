from selenium.webdriver.common.by import By


class Tasks(object):
    # A class for NavBar locators. All locators should come here
    TO_BE_DONE_TABLE_HEAD = (By.CLASS_NAME, 'panel-heading')
    TO_DO_HEAD_LABEL = (By.TAG_NAME, 'h1')
    NEW_TASK_FORM = (By.ID, 'new_task')
    ADD_BUTTON = (By.CLASS_NAME, 'glyphicon-plus')
    FIRST_TASK_ON_THE_LIST_LINK_TEXT = (By.CSS_SELECTOR, 'body > div.container > div.task_container.ng-scope > div.bs-example > div > table > tbody > tr:nth-child(1) > td.task_body.col-md-7 > a')
