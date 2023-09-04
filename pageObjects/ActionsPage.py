import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""THIS PAGE CONTAINS ALL THE GENERIC METHODS AND UTILITIES"""
class BasePage:
#INISTATING THE DRIVER FUNCTION
    def __init__(self, driver):
        self.driver = driver

#TO PERFORM CLICK OPERATION
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

# TO PERFORM SEND KEYS OPERATION
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

# TO GET ELEMENT TEXT OPERATION
    def get_element_text(self, by_locator):
        element  = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

#TO FIND AN ELEMENT IS VISISBLE OPERATION
    def is_visible(self, by_locator):
        element  = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
#TO SEND ENTER KEY
    def click_enter_key(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

#TO SEND ENTER KEY
    def click_clear_key(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.CLEAR).perform()

#TO GET THE TITLE OF A PAGE
    def get_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title