import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try :
        textarea = driver.find_element(By.NAME,"q")
        driver.refresh()
        # DOM elements - refreshed
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS
        # webdriver throws stale element exception
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("The testing academy")
    except StaleElementReferenceException as see:
        print(see)
        # driver.switch_to.alert --> NoAlertPresentException

    time.sleep(5)
    driver.quit()