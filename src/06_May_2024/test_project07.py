import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

def test_project07():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    time.sleep(5)
    driver.switch_to.frame("result") #we can directly give id instead of driver.findelement
    #driver.find_element(By.XPATH, "//iframe[@id='result']"))  # HTML document is in Iframe, switching the window

    submit = driver.find_element(By.XPATH, "//button[text() = 'Submit']")
    submit.click()
    message = driver.find_element(locate_with(By.TAG_NAME, 'small').below({By.ID: 'username'})).text
    assert message == "Username must be at least 3 characters"
    time.sleep(5)
    driver.quit()