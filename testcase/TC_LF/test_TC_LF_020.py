from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_020
# Validate the different ways of navigating to the Login page


def test_TC_LF_020(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()
    lp = LoginPage(driver)
    assert lp.login_button_displaystatus() is True
    lp.continue_button()
    rp = RegisterPage(driver)
    rp.clicklogin_link_registerpage()
    assert lp.login_button_displaystatus() is True