import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cure_tagname():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #finding the element with 'a' tag
    list_of_tags = driver.find_elements(By.TAG_NAME, "a") #find_elements() returns list of elements
    make_appointment_btn = list_of_tags[5] #make appointment button is in 6th anchor(a) tag
    make_appointment_btn.click()

    time.sleep(20)

    driver.quit()