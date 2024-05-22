import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_01_JS1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    # Javascript executor
    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    time.sleep(3)
    #button.click()
    driver.execute_script("arguments[0].click()",button)
    driver.execute_script("arguments[0].click()",button)
    time.sleep(5)
    driver.quit()