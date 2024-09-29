from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


# TC_RF_020
# Validate whether the 'Privacy Policy' checkbox option is not selected by default

def test_TC_RF_001(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    status = rp.privacy_agree_status()
    if status == True:
        assert False