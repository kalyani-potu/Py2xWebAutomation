from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome() # POST request | Create the Session
    driver.get("https://app.vwo.com") # GET Request to URL param
    driver.maximize_window()
    print(driver.session_id)
    print(driver.page_source)
    print(driver.title) #prints title of the page
    assert driver.title == "Login - VWO"