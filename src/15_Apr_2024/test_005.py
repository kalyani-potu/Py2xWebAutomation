from selenium import webdriver
import time

def test_open_window():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(10) # Python Interpreter waits for the 25 seconds, not the webdriver.
    driver.back() #back to the blank chrome window
    time.sleep(10)
    driver.get("https://www.google.com")
    print(driver.title)
    time.sleep(10)

    driver.back()
    print(driver.title)
    time.sleep(10)

    driver.forward()
    print(driver.title)
    time.sleep(10)



    driver.refresh()
    time.sleep(5)

    driver.quit()

