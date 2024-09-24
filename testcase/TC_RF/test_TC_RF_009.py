import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage

from utilities import randomstring
from utilities.logger_utility import LoggerUtility

from utilities.readproperty import ReadConfig


# Validate Registering an Account by providing the existing account details (i.e. existing email address)
# TC_RF_009

def test_TC_RF_008(setup):

    logger = LoggerUtility().get_logger()
    logger.info("**** test_TC_RF_009 started *** ")
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
    # email = randomstring.random_string_generator() + '@gmail.com'

    rp.enter_email(ReadConfig.getUseremail())
    rp.enter_phone("9762629797")
    rp.enter_password(ReadConfig.getPassword())
    rp.enter_cpassword(ReadConfig.getPassword())
    rp.click_agree()
    rp.click_continue()

    actual_result = rp.already_registered()
    expected_result = "Warning: E-Mail Address is already registered!"

    print(actual_result)

    if actual_result == expected_result:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_009.png')
        logger.error("Already Registered Alert Not Shown")
        assert False

    logger.info("**** test_TC_RF_009 Ended *** ")