from selenium import webdriver

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_017
# Validate Logging into the Application, closing the Browser without loggingout and opening the application in the Browser again


def test_TC_LF_017(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(ReadConfig.getPassword())
    lg.click_login()
    assert lg.is_logout_present(), "User login failed, logout option not found!"

    cookies = driver.get_cookies()

    driver = webdriver.Chrome()
    driver.get(ReadConfig.getApplicationURL())
    for i in cookies:
        driver.add_cookie(i)
    driver.refresh()

    assert lg.is_logout_present(), "User session was not maintained after reopening the browser!"
