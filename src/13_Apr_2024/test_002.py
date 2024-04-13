from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # Python Intepreter -> optimize if there is no command, It will stop the execution.