import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage

from utilities import randomstring
from utilities.readproperty import ReadConfig


# Validate Registering an Account when 'Yes' option is selected for Newsletter field
# TC_RF_005

def test_TC_RF_005(setup):

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
    status = rp.subscribe_yes()
    status.click()
    rp.click_agree()
    rp.click_continue()
    rp.continue_btnsucces()
    actual_result = rp.subscribe_option()
    print(actual_result)
    expected_result = "Subscribe / unsubscribe to newsletter"

    if actual_result == expected_result:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_005.png')
        assert False