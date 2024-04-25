import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    username = driver.find_element(By.XPATH, value="//input[@name='username']")
    username.send_keys("admin")

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
