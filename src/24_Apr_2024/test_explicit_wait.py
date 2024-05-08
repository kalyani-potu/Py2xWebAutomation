import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email_input = driver.find_element(By.CSS_SELECTOR, value="[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, value='[name="password"]')
    email_input.send_keys("admintyuu@gmail.com")
    pass_input.send_keys("adminkkk")
    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()
    # error_msg_element - comes after 5 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # pageTile = vwo.com
    # error -> visible -> move forward
    # erorr msg is seen on the DOM (html) - i will read the text

    # Explicit Wait

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )
    error_msg  = driver.find_element(By.ID, value = "js-notification-box-msg")
    assert error_msg.text == "Your email, password, IP address or location did not match"
    allure.attach(driver.get_screenshot_as_png(), name="login-error-msg", attachment_type=AttachmentType.PNG)
    driver.quit()