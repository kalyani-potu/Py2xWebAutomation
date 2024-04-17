from selenium import webdriver
import time
def test_open_vwologin():
    driver = webdriver.Chrome()
    time.sleep(20)
    # Session is created - Unique ID - 16 digit ID
    # 64avbdas6a6d89as9a7 - Session?
    # webdriver.chrome() - fresh copy of browser is created
    # open new tabs, open url, those will be different from the normal browser. - Automation.
    # everything is deleted.