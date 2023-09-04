from config.config import TestData
from testCases.test_base import BaseTest
from pageObjects.ActionsPage import BasePage
from pageObjects.LoginPage import LoginPage
from pageObjects.EventsPage import EventPage

from selenium.webdriver.common.by import By

class Test_Events(BaseTest):
    def test_event_new(self):
        driver = BaseTest.driver
        driver.get("https://console.horse.mycoachapp.org/")
        #IMPORTING THE LoginPage INTO loginpage
        self.loginpage = LoginPage(driver)
        #IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.loginpage.do_login(TestData.EMAIL, TestData.PASSWORD)
        #IMPORTING THE EventPage INTO eventpage
        self.eventpage = EventPage(self.driver)
        #IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.eventpage.create_event(TestData.TERM, TestData.EVENT_TITLE, TestData.EVENT_DATE, TestData.EVENT_DETAILS)

