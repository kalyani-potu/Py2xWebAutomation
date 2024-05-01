import time
import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify the error message that comes when username is not passed.")
@allure.description("TC#01 - click submit button without passing username, verify the error message")
def test_codepen_no_username_error():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='result']"))
    time.sleep(3)
    email = driver.find_element(By.XPATH, value="//input[@id='email']")
    email.send_keys("kalyani.p@gmail.com")
    password = driver.find_element(By.XPATH, value="//input[@id='password']")
    password.send_keys("123456")
    confirm_password = driver.find_element(By.XPATH, value="//input[@id='password2']")
    confirm_password.send_keys("123456")
    submit_btn = driver.find_element(By.XPATH, value="//button[text()='Submit']")
    submit_btn.click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="error-screenshot", attachment_type=AttachmentType.PNG)
    username_error_msg = driver.find_element(By.XPATH, value="//input[@id='username']/following-sibling::small")
    #//small[text()= 'Username must be at least 3 characters'] this xpath doen't work because text is dynamic,
    #it is better to use other attributes instead of text(), whenever text is modified , testcases will fail or regression will fail
    # username_error_msg = driver.find_element(By.XPATH, username+"/following-sibling::small") # concatination doesnot work on webelement
    print(username_error_msg.text)
    assert username_error_msg.text == "Username must be at least 3 characters"
    time.sleep(2)
    driver.quit()

