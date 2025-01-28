from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig

# TC_LF_015
# Validate the Password is not visible in the Page Source

def test_TC_LF_015(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    password = ReadConfig.getPassword()
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(password)

    page_source = driver.page_source

    if password not in page_source:
        assert True ,f"Password Not in Page Source"
    else:
        assert False ,f"Password Present in Page Source"

    lg.click_login()

    after_page_source = driver.page_source

    if password not in after_page_source:
        assert True ,f"Password Not in Page Source after Login"
    else:
        assert False ,f"Password Present in Page Source after Login"


