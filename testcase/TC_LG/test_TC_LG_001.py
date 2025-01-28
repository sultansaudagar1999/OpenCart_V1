from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from pageobjects.TS_003_Logout_Functionality.LogoutPage import LogoutPage
from utilities.readproperty import ReadConfig


# TC_LG_001
# Validate Logging out by selecting Logout option from 'My Account' dropmenu

def test_TC_LG_001(setup):

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

    lg.myaccount_drpdown()
    lg.click_logout()

    lg = LogoutPage(driver)
    lg.logoutpage_continue_button()

    act_url = driver.current_url
    exp_url = "https://naveenautomationlabs.com/opencart/index.php?route=common/home"



    assert act_url == exp_url
