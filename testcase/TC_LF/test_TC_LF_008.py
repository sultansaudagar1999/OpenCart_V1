from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_008
# Validate E-Mail Address and Password text fields in the Login page have the place holder text.


def test_TC_LF_008(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    act_email = lg.email_placeholder()
    act_password = lg.password_placeholder()

    exp_email = "E-Mail Address"
    exp_password = "Password"
    assert act_email == exp_email and act_password == exp_password

