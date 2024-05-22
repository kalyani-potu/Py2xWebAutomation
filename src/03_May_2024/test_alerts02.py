import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_alerts01():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    alert_element = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    alert_element.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert_popup = driver.switch_to.alert
    alert_popup.accept() #ok

    # popups -> model or html popup, alert - this how handle
    # wait for the model to come and click on the escape button, or close button
    result = driver.find_element(By.ID, 'result')
    print(result.text)
    assert result.text == "You successfully clicked an alert"
    time.sleep(3)
    driver.quit()