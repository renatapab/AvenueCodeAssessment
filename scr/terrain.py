from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    world.browser = webdriver.Chrome('C:/Projetos/configs/chromedriver_win32/chromedriver')
