from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome() # POST request | Create the Session
    # Session is created - Unique ID - 16 digit ID
    # 64avbdas6a6d89as9a7 - Session?
    # webdriver.Chomre() - fresh copy of browser is created
    # opens new tabs, opens url, those will be different from the normal browser.

    driver.get("https://app.vwo.com") # GET Request to URL param
    driver.maximize_window()
    print(driver.session_id)
    print(driver.page_source)
    print(driver.title) #prints title of the page
    assert driver.title == "Login - VWO"