from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_018
# Validate timeout of the Login Session


def test_TC_LF_018(setup):
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
    #time.sleep(1800) wait for 30 minutes
    assert lg.myaccount_page() == True