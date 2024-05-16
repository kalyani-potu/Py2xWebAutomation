import time
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    atag = driver.find_element(By.ID, "click")

    # Click - Normal click will find the element and click on it, release it
    # Click and Hold -> Click -> and Hold, we will not release it.
    ActionChains(driver).click_and_hold(atag).perform()
    time.sleep(5)
    driver.quit()

