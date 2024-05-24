import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def test_googlesearch():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    input = driver.find_element(By.NAME ,'q')
    input.send_keys("Gmail")
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.quit()
