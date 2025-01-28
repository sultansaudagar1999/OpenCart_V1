from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_002
# Validate logging into the Application using invalid credentials (i.e. Invalid email address and Invalid Password)

def test_TC_LF_002(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email("sultan1267@gmail.com")
    lg.enter_password("123654")
    lg.click_login()

    actual_result = lg.myaccount_page()

    if actual_result == True:
        assert False
    else:
        assert True