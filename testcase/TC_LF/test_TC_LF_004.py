from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_004
# Validate logging into the Application using valid email address and invalid Password

def test_TC_LF_004(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password("321123")
    lg.click_login()

    actual_result = lg.myaccount_page()

    if actual_result == True:
        assert False
    else:
        assert True