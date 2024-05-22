import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_shadow01():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    time.sleep(15)
    div = driver.find_element(By.XPATH, "//div[@class = 'jackPart']")
    #java executer script
    driver.execute_script("arguments[0].scrollIntoView(true);", div) # Scroll to View to DIV,
    # we can scroll to that section where pizza input is present using java executor, but without scrolling also, next steps doesn't fail
    time.sleep(5)
    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("olivepizza")
    time.sleep(5)
    driver.quit()