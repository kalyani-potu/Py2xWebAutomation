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
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname, "the testing academy").key_up(Keys.SHIFT).context_click().perform()
    #perform(): perform method performs all the actions stored inside an actions object
    #context_click() == > right click
    time.sleep(10)
    driver.quit()

