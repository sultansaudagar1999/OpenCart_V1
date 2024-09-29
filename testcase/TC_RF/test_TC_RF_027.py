from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


def test_TC_RF_027(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Navigate to the register page
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    act_status = rp.register_page()
    exp_status = "Register Account"

    if act_status == exp_status:
        assert True
    else:
        assert False