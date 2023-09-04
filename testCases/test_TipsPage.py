from config.config import TestData
from testCases.test_base import BaseTest
from pageObjects.ActionsPage import BasePage
from pageObjects.LoginPage import LoginPage
from pageObjects.TipsPage import TipsPage
from selenium.webdriver.common.by import By

class Test_Tips(BaseTest):
    def test_tip_new(self):
        #IMPORTING THE LoginPage INTO loginpage
        self.loginpage = LoginPage(self.driver)
        # IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.loginpage.do_login(TestData.EMAIL, TestData.PASSWORD)
        #IMPORTING THE TipsPage INTO tipspage
        self.tipspage = TipsPage(self.driver)
        # IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.tipspage.create_tip(TestData.CALL_TO_ACTION, TestData.TIPS_TITLE, TestData.TIP_DETAILS, TestData.DATE)