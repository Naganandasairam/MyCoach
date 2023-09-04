from pageObjects.ActionsPage import BasePage
from config.config import TestData
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
#PATH'S USED IN LOGIN PAGE
    Email = (By.NAME, "email")
    Password = (By.NAME, "password")
    Submit = (By.XPATH, "//button[@type='submit']")
#PATH'S USED IN SETTINGS
    Settings = (By.XPATH, "//button[@aria-label='User Options']")
    MyProfile = (By.XPATH, "//a[normalize-space()='My Profile']")
    LogOut = (By.XPATH, "//a[normalize-space()='Logout']")
#PATH'S USED FOR FORGOT PASSWORD
    Forgot_password_error = (By.XPATH, "//a[@href='/forgot-pass']") #//a[@href='/forgot-password']

#PATH'S USED IN PAGE
    Edit_btn = (By.XPATH, "//form//div//div//button[normalize-space()='Edit']")
    First_name = (By.NAME, "first_name")
    Save_Changes = (By.XPATH, "//button[normalize-space()='Save Changes']")

#THIS FUNCTION IS INVOKE THE MYCOACH CONSOLE
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.baseURL)

#THIS FUNCTION IS FOR LOGGING INTO CONSOLE
    def do_login(self, username, password):
        self.do_click(self.Email)
        self.do_send_keys(self.Email, username)
        self.do_click(self.Password)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Submit)

#THIS FUNCTION IS FOR LOGGING OUT FROM THE CONSOLE
    def do_logout(self):
        self.do_click(self.Settings)
        self.do_click(self.LogOut)

#THIS FUNCTION IS FOR LOGGING OUT FROM THE CONSOLE
    def do_forgot(self):
        self.do_click(self.Forgot_password_error)