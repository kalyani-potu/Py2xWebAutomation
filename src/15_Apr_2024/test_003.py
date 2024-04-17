from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com") # GET Request to URL param
    driver.maximize_window()
    print(driver.session_id)
    print(driver.title)
    assert driver.title == "Login - VWO"

    time.sleep(10)

    driver.quit()
    # Close all the windows or tabs
    # session id == null, ends the browser session completely
    # It will close all the other tabs.
    time.sleep(10)