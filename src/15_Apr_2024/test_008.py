from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_cura():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg" >Make Appointment</a>

    # Find the element the anchor tag - button
    # Click on it

    # #1 - id, className, name, tagName, linkText and PartialLinkText.
    # #2 - css Selector, xpath(sure shot way to find the elements in the HTML)

    element = driver.find_element(By.ID, value="btn-make-appointment")
    time.sleep(5)
    element.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    driver.quit()