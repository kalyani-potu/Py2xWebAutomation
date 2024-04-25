import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify the trial end error message in idrive360.com website")
@allure.description("TC#1 - Trial end error message on idrive360.com Website.")
def test_idrive360login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.XPATH, value="//input[@name='username']")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.XPATH, value="//input[@id='password']")
    password.send_keys("123456")

    submit_btn = driver.find_element(By.ID, value="frm-btn")
    submit_btn.click()

    time.sleep(20)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Assertion Fail Message #1 - Error Matching the URLs"

    message = driver.find_element(By.XPATH, value="//h5[@class='id-card-title']")
    assert  message.text == "Your free trial has expired"


    allure.attach(driver.get_screenshot_as_png(), name="trial-end-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
