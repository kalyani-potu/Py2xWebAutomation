import time
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    firstname = driver.find_element(By.XPATH, value= "//input[@name = 'firstname']")
    # Shirt Down + types + Shift Up
    #first letter capital and rest of the letters small
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname, "t").key_up(Keys.SHIFT).send_keys("he testing academy").perform()

    #perform(): perform method performs all the actions stored inside an actions object
    #actions.send_keys("the testing academy").perform()
    time.sleep(10)
    driver.quit()

