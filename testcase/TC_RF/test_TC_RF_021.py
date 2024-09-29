from wsgiref.validate import assert_

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.readproperty import ReadConfig


# TC_RF_021
# Validate Registering the Account without selecting the 'Privacy Policy' checkbox option

def test_TC_RF_001(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    rp.enter_firstname("Sultan")
    rp.enter_lastname("Saudagar")
    email = randomstring.random_string_generator() + '@gmail.com'
    rp.enter_email(email)
    rp.enter_phone("9762629797")
    rp.enter_password(ReadConfig.getPassword())
    rp.enter_cpassword(ReadConfig.getPassword())
    rp.click_continue()
    act_result = rp.warning_tcaccept()
    print(act_result)
    exp_result = "Warning: You must agree to the Privacy Policy!"
    if act_result == exp_result:
        assert True
    else:
        assert False