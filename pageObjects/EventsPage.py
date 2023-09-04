from pageObjects.ActionsPage import BasePage
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class EventPage(BasePage):
#PATH'S USED IN EVENT'S PAGE
    Event_Addnew = (By.XPATH, "//a[@ng-href='/events/add']")
    Term_sel = (By.XPATH, "//input[@placeholder='Term']")
    Term_selection = (By.XPATH, "//li[@role='option']")
    Event_title = (By.XPATH, "//div//md-input-container//input[@name='name']")
    Event_Date = (By.XPATH, "//input[@name='start_date']")
    Event_Details = (By.XPATH, "//iframe[@title='Rich Text Area']")
    Category = (By.XPATH, "//md-select[@aria-label='Category']")
    Category_Ac_DeadLine = (By.XPATH, "//md-option[normalize-space()='Academic Deadline']")
    #Save_btn = (By.XPATH, "//button[normalize-space()='Save']")
    Save_btn = (By.XPATH, "//footer[1][@md-whiteframe='2']//span")

#PATH USED TO CLICK THE EVENT IS DISPLAYED ON THE TOP
    Created_event = (By.XPATH, "//div[@md-virtual-repeat='item in ctrl'][1]//h3")

#THIS IS FOR DELETING AN EVENT
    Delete_btn = (By.XPATH, "//button[normalize-space()='Delete'][1]")
    Popup_delete_btn = (By.XPATH, "//button[@ng-click='dialog.hide()']")

#INVOKING THE DRIVER
    def __init__(self, driver):
        super().__init__(driver)

#FUNCTION USED TO CREATE AN EVENT
    def create_event(self, term, event_title, event_date, event_details):
        self.do_click(self.Event_Addnew)
        self.do_click(self.Term_sel)
        self.do_send_keys(self.Term_sel, term)
        self.do_click(self.Term_selection)
        self.click_enter_key()
        self.do_click(self.Event_title)
        self.do_send_keys(self.Event_title, event_title)
        self.do_click(self.Event_Date)
        self.do_send_keys(self.Event_Date, event_date)
        self.do_click(self.Event_Details)
        self.do_send_keys(self.Event_Details, event_details)
        self.do_click(self.Category)
        self.do_click(self.Category_Ac_DeadLine)
        self.do_click(self.Save_btn)

#FUNCTION USED TO CLICK THE FIRST EVENT DISPLAYED
    #def new_created_event_visible(self):
     #   return self.is_visible(self.created_event)
