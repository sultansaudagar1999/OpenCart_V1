from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.ForgotPasswordPage import ForgotPasswordPage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_006
# Validate 'Forgotten Password' link is available in the Login page and is working

def test_TC_LF_006(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.click_forgot_password()
    fp = ForgotPasswordPage(driver)

    actual_result = fp.email_box_status()

    if actual_result == True:
        assert True
    else:
        assert False