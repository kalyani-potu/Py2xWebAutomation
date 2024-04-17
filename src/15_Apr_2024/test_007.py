from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    # id -> name -> className -> tagName -> LinkText, PartialText -> css Selector -> Xpath

    #< input type = "email" class ="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi" >

    email_element = driver.find_element(By.NAME, value="username")
    email_element.send_keys("admin") #send_keys function is used to pass the values

    #< input type = "password" class ="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe" aria-autocomplete="list" >

    password_element = driver.find_element(By.ID, value="login-password")
    password_element.send_keys("admin")

    submit_button_element = driver.find_element(By.ID, value="js-login-btn")
    submit_button_element.click()

    time.sleep(5)

    error_msg_element = driver.find_element(By.ID, value="js-notification-box-msg")
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()
