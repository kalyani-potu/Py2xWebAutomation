import random

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.smoke
@allure.title("Verify the user on OrangeHRM website")
@allure.description("TC#1 - Logon to OrangeHRM, add a user and verify the user")
def test_orange_hrm():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    login_name = driver.find_element(By.XPATH, "//input[@name='username']")
    login_pswd = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_name.send_keys("Admin")
    login_pswd.send_keys("admin123")
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Admin']"))
    )
    admin_element = driver.find_element(By.XPATH,"//span[text()='Admin']" )
    admin_element.click()
    WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()=' Add ']"))
    )
# Adding User
    add_button = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    add_button.click()
    WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Add User']"))
    )

    #user role dropdown
    role_select = driver.find_element(
        By.XPATH, "//label[text()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//*/i"
    )
    #above Xpath is same as-->
    #"//label[text()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/div/div/div/div/i")
    role_select.click()

    #selecting admin from the dropdown
    admin_element= driver.find_element(By.XPATH, "//div[@role='listbox']/div[2]/span[text()='Admin']")
    admin_element.click()

    #employee name field
    employee_name = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_name.send_keys("Ra")
    WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Ravi M B']"))#//div[@class='oxd-autocomplete-option']/span[text()='Ravi M B']
    )
    #selecting the employee name
    driver.find_element(By.XPATH, "//span[text()='Ravi M B']").click()

    #Status dropdown
    status_select = driver.find_element(
        By.XPATH, "//label[text()='Status']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//*/i"
    )
    status_select.click()
    #selecting enabled from dropdown
    enabled_element= driver.find_element(By.XPATH, "//div[@role='listbox']/div[2]/span[text()='Enabled']")
    enabled_element.click()

    #username
    username = "person" + str(random.randint(111,888))
    username_element =driver.find_element(By.XPATH, "//label[text()='Username']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input")
    username_element.send_keys(username)
    #password and confirm password
    password_element = driver.find_elements(By.XPATH, "//input[@type = 'password']")
    password_element[0].send_keys("password123")
    password_element[1].send_keys("password123")

    save_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_btn.click()

    WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[text()='System Users']"))
    )

#search user
    search_username = driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input[@class = 'oxd-input oxd-input--active']")
    search_username.send_keys(username)

    search_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_btn.click()

    WebDriverWait(driver,timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']"))
    )
#asserting user
    result = driver.find_elements(By.XPATH, "//div[@class = 'oxd-table-cell oxd-padding-cell']")
    assert result[1].text == username
    assert result[2].text == "Admin"
    assert result[3].text == "Ravi B"
    assert result[4].text == "Enabled"
    allure.attach(driver.get_screenshot_as_png(), name="user verification screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()