import allure
import time
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
@pytest.mark.smoke
@allure.title("Find SVG element in flipkart")
@allure.description("TC#01 - Find search button and click on it")
def test_svg_flkt():
        driver = webdriver.Chrome()
        driver.get("https://flipkart.com")
        driver.maximize_window()
        time.sleep(3)
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.send_keys("AC")
        svg_list = driver.find_elements(By.XPATH, "//*[name()='svg']")
        svg_list[0].click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),name="flipkart_screenshot", attachment_type=AttachmentType.PNG)
        driver.quit()