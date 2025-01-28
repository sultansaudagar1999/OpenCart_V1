from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_023
# Validate the Login page functionality in all the supported environments


def test_TC_LF_023(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()
    lp = LoginPage(driver)
    assert lp.login_button_displaystatus() is True