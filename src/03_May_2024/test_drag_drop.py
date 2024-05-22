import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def test_alerts01():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    from_element = driver.find_element(By.ID, "column-a")
    to_element = driver.find_element(By.ID, "column-b")

    actions = ActionChains(driver)
    actions.click_and_hold(from_element).move_to_element(to_element).release(to_element).perform()
    #actions.drag_and_drop(from_element,to_element).perform()


    time.sleep(10)
    driver.quit()