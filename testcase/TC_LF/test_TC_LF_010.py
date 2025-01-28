from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_010
# Validate Loggingout from the Application and browsing back using Browser back button

def test_TC_LF_010(setup):

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
    driver.back()
    driver.refresh()

    assert lg.myaccount_page() == False