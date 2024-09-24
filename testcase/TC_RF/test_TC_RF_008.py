import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage

from utilities import randomstring
from utilities.logger_utility import LoggerUtility

from utilities.readproperty import ReadConfig


# Validate Registering an Account by entering different passwords into 'Password' and 'Password Confirm' fields
# TC_RF_008

def test_TC_RF_008(setup):

    logger = LoggerUtility().get_logger()
    logger.info("**** test_TC_RF_008 started *** ")
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
    rp.enter_cpassword("sultan@12345")
    rp.click_agree()
    rp.click_continue()
    actual_result = rp.password_mismatch()
    expected_result = "Password confirmation does not match password!!"

    print(actual_result)

    if actual_result == expected_result:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_008.png')
        logger.error("Password mismatch alert not shown..!")
        assert False

    logger.info("**** test_TC_RF_008 Ended *** ")




