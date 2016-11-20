from lettuce import *
from lettuce import world
from lettuce_webdriver import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
    world.browser.implicitly_wait(1)

@after.all
def tear_down_feature(feature):
    world.browser.quit()
