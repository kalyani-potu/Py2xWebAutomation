import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

def test_relative():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    driver.find_element(locate_with(By.ID, "exp-3").to_right_of({By.XPATH : "//span[text()='Years of Experience']"})).click()
    time.sleep(3)
    driver.quit()
