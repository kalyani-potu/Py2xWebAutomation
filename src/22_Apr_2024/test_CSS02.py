import time

import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.title("Verify that Login is working in Cura website")
@allure.description("TC#1 - Simple Login check on CURA katalong Website.")
def test_cura_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn = driver.find_elements(By.CSS_SELECTOR, value='.btn.btn-dark.btn-lg')
    make_appointment_btn[1].click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    allure.attach(driver.get_screenshot_as_png(), name = "login screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    driver.quit()
