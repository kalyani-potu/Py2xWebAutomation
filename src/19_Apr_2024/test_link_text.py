import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_curalogin_link_text():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # By. Link Text - Full Match or Exact match with the Text
    # rule 1 - first one, if there is no link text it will not able to find the element
    # a tag -> anchor tag

    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    make_appointment_btn = driver.find_element(By.LINK_TEXT, value="Make Appointment")
    make_appointment_btn.click()
    time.sleep(10)
    driver.quit()