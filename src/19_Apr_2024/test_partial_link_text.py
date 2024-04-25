import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_curalogin_link_text():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Partial Text
    # a anchor
    # partial match

    # Make Appointment
    # Appointment
    # Make
    # App
    # ment
    # Contains - keyword
    # Find the first unique element


    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, value="Appointment")
    make_appointment_btn.click()
    time.sleep(10)
    driver.quit()

    # ID - Unique ID
    # name, Unique ClassName,
    # TagName - get 1 from list of elements via findElements
    # Link/ partial - 'a' anchor tags
    # Css Selector - 20%
    # XPath - 60% used