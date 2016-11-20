from scr.pages.page_login import PageLogin
from lettuce import step, world
from selenium import webdriver

@step("I'm logged in")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    step.b
