from pageObjects.ActionsPage import BasePage
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class TipsPage(BasePage):
#PATH'S USED IN TIP'S PAGE
    Tips_sec = (By.XPATH, "//md-list-item[@ng-href='/tips']")
    Tips_Addnew = (By.XPATH, "//a[@ng-href='/tips/add']")
    Level_sel = (By.XPATH, "//input[@placeholder='Level']")
    Level_selection = (By.XPATH, "//li[@role='option']")
    Tips_title = (By.XPATH, "//div//md-input-container//input[@name='name']")
    Call_to_Action = (By.XPATH, "//md-input-container//textarea[@name='call_to_action']")
    Background_colour = (By.XPATH, "//md-select[@name='background_color']")
    Bgcolour_selection = (By.XPATH, "//md-content[@aria-label='Background Color']//md-option[@role='option'][2]")
    Tips_Details = (By.XPATH, "//iframe[@title='Rich Text Area']")
    Date_to_Send = (By.NAME, "date_to_send")
    Category = (By.XPATH, "//md-input-container//md-select[@aria-label='category']")
    Category_Ac_DeadLine = (By.XPATH, "//md-option[normalize-space()='Academic Deadline']")
    Save_btn = (By.XPATH, "//button[normalize-space()='Save']")

#INVOKING THE DRIVER
    def __init__(self, driver):
        super().__init__(driver)

#FUNCTION USED TO CREATE AN EVENT
    def create_tip(self, call_to_action, tips_title, tips_details, date): #level,
        self.do_click(self.Tips_sec)
        self.do_click(self.Tips_Addnew)
        self.do_click(self.Level_sel)
        self.do_click(self.Tips_title)
        self.do_click(self.Call_to_Action)
        self.do_send_keys(self.Call_to_Action, call_to_action)
        self.do_click(self.Tips_title)
        self.do_send_keys(self.Tips_title, tips_title)
        self.do_click(self.Tips_Details)
        self.do_send_keys(self.Tips_Details, tips_details)
        self.do_click(self.Date_to_Send)
        self.do_send_keys(self.Date_to_Send, date)
        self.do_click(self.Category)
        self.do_click(self.Category_Ac_DeadLine)
        self.do_click(self.Save_btn)