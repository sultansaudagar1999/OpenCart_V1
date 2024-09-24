import os

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


#TC_RF_007
# Validate different ways of navigating to 'Register Account' page

def test_TC_RF_007(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lp = LoginPage(driver)
    lp.continue_button()

    rg = RegisterPage(driver)

    actual_result = rg.register_page()
    expected_result = "Register Account"

    if actual_result == expected_result:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_007.png')
        assert False

