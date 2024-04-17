from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_cura():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    element_appointment.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    element_username = driver.find_element(By.ID, value="txt-username")
    element_username.send_keys("John Doe")
    element_password = driver.find_element(By.ID, value="txt-password")
    element_password.send_keys("ThisIsNotAPassword")
    element_button = driver.find_element(By.ID, value="btn-login")
    element_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(3)
    #< div  class ="col-sm-12 text-center" >
    #< h2 > Make Appointment < / h2 >
    #< hr class ="small" >
    # < / div >
    element_appt_txt = driver.find_element(By.CLASS_NAME, value="col-sm-12")
    assert element_appt_txt.text == "Make Appointment"
    driver.quit()