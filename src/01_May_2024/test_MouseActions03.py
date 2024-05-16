import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    hover_element = driver.find_element(By.ID, "hover")
    time.sleep(3)
    #mouse hovering over the element
    ActionChains(driver).move_to_element(hover_element).pause(5).perform()
    driver.quit()