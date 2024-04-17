from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com") # GET Request to URL param
    driver.maximize_window()
    print(driver.session_id)
    print(driver.title)
    assert driver.title == "Login - VWO"

    driver.close()
    # Close will close the current window or tab.
    # session id != null(Invalid)
    # It will not close the other tabs.
    time.sleep(10)