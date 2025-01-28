from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.ChangePasswordPage import ChangePasswordPage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from testcase.TC_RF.conftest import setup
from utilities.readproperty import ReadConfig


# Validate logging into the Application using valid credentials
# TC_LF_001

def test_TC_LF_016(setup):

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

    lg.change_your_password()

    new_password = "123456"
    cp = ChangePasswordPage(driver)
    cp.enter_password(new_password)
    cp.enter_confirm_password(new_password)
    cp.continue_button()

    lg.myaccount_drpdown()
    lg.click_logout()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(ReadConfig.getPassword())
    lg.click_login()
    
    assert lg.myaccount_page() == False

    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(new_password)
    lg.click_login()

    assert lg.myaccount_page() == True




