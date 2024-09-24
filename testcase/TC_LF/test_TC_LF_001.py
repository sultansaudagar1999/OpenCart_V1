import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from testcase.TC_RF.conftest import setup
from utilities.readproperty import ReadConfig


# Validate logging into the Application using valid credentials
# TC_LF_001

def test_TC_LF_001(setup):

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

    actual_result = lg.myaccount_page()
    expected_result = "My Account"

    if actual_result == expected_result:
        assert True
    else:
        assert False


    time.sleep(5)

