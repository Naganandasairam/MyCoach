import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData

"""This Conftest file is used to get chrome driver"""
@pytest.fixture(scope='class')
def init_driver(request):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # ... Automate something here
    #driver.quit()

    #CHROME_EXECUTABLE_PATH HAS THE CHROME DRIVER PATH WHICH IS STORED IN CONFIG.PY FILE
   # Chrome_service = Service(TestData.CHROME_EXECUTABLE_PATH)

    print(TestData.CHROME_EXECUTABLE_PATH+"druver path")
    #web_driver = webdriver.Chrome(service=Chrome_service)
    driver.maximize_window()
    #request.cls.driver = web_driver

    #CLOSING THE BROWSER AFTER EXECUTION
    yield
    #driver.close()