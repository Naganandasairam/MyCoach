from config.config import TestData
from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest

class Test_LoginPage(BaseTest):
#THIS IS THE LOGIN TESTCASES USING AN USERNAME AND A PASSWORD
    def test_login(self):
        # IMPORTING THE LoginPage INTO loginpage
        self.loginpage = LoginPage(self.driver)
        # IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.loginpage.do_login(TestData.EMAIL, TestData.PASSWORD)

#THIS IS A LOGOUT TESTCASE
    def test_logout(self):
        # IMPORTING THE LoginPage INTO loginpage
        self.loginpage = LoginPage(self.driver)
        # IMPORTING THE REQUIRED DATA FROM TESTDATA CLASS
        self.loginpage.do_login(TestData.EMAIL, TestData.PASSWORD)
        #PERFORMING THE LOGOUT OPERATION
        self.loginpage.do_logout()

#THIS IS FORGOT PASSWORD TESTCASE
    def test_forgot_password(self):
        # IMPORTING THE LoginPage INTO loginpage
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_forgot()