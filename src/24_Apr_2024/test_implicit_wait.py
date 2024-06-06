import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Implicit wait tells the WebDriver to wait for a certain amount of time before throwing a NoSuchElementException. It is set once and applies to all elements in the WebDriver instance.
    driver.get("https://app.vwo.com")
    # e1, e2 , e3 ->
    # Tell Webdriver to wait for the 5 to Load
    # All the elements.
    # What if the e1,e2,e3 < 3, then 2 wasted.
    email_input = driver.find_element(By.CSS_SELECTOR, value="[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, value='[name="password"]')
    email_input.send_keys("admintyuu@gmail.com")
    pass_input.send_keys("adminkkk")
    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()
    # Python - Int - It is super bad practice - time.sleep(5) - Worst type of Wait.
    time.sleep(5) # This is Python Int who is waiting, Python Execution Halt.

    error_msg  = driver.find_element(By.ID, value = "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"
    allure.attach(driver.get_screenshot_as_png(), name="login-error-msg", attachment_type=AttachmentType.PNG)
    driver.quit()