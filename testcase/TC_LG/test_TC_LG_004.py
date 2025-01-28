import time
from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from pageobjects.TS_003_Logout_Functionality.LogoutPage import LogoutPage
from utilities.readproperty import ReadConfig
#
# TC_LG_004
# Validate logging out and browsing back

# Failed

def test_TC_LG_004(setup):
    # Step 1: Open the browser and navigate to the application
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Step 2: Perform login
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(ReadConfig.getPassword())
    lg.click_login()
    lg.click_logout()

    driver.back()

    assert lg.myaccount_page() == False



