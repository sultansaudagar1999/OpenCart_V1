from selenium.webdriver import ActionChains, Keys

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_007
# Validate logging into the Application using Keyboard keys (Tab and Enter)

def test_TC_LF_007(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    act = ActionChains(driver)
    act.key_down(Keys.TAB).send_keys(ReadConfig.getPassword()).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    act.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

    actual_result = lg.myaccount_page()

    if actual_result == True:
        assert True
    else:
        assert False