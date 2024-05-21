import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("Finding SVG in maps")
@allure.description("TC#1 - Find and click on a state SVG element")
def test_svg_map():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)
    states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states:
        if "Tripura" in state.get_attribute("aria-label"):
            print(state.get_attribute("aria-label")) #aria-label is attribute name, get_attribute("aria-label") returns attribute value
            state.click()
            break
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="svg_elements", attachment_type=AttachmentType.PNG)
    driver.quit()

