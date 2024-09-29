from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_RF_023
# Validate navigating to other pages using the options or links provided on the 'Register Account' page

def test_TC_RF_023(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    rp.clicklogin_link_registerpage()

    lp = LoginPage(driver)
    login_page_status = lp.login_button_displaystatus()

    if login_page_status == True:
        assert True
    else:
        assert False