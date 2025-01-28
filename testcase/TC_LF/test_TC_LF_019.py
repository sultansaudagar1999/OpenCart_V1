# TC_LF_019
# Validate user is able to navigate to different pages from Login page
from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.ForgotPasswordPage import ForgotPasswordPage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from testcase.TC_LF.conftest import setup
from utilities.readproperty import ReadConfig


def test_TC_LF_019(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.continue_button()
    assert lg.register_page_status() is True
    driver.back()
    lg.click_forgot_password()
    fp = ForgotPasswordPage(driver)
    assert fp.forgot_page_status() is True

