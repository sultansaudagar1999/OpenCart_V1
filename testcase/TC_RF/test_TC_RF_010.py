import os

import pytest

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.logger_utility import LoggerUtility
from utilities.readproperty import ReadConfig


# Validate Registering an Account by providing an invalid email address into the E-Mail field
# TC_RF_010

@pytest.mark.parametrize('email',[("pavanol"),("pavanol@"),("pavanol@gmail"),("pavanol@gmail.com")])
def test_TC_RF_010(setup,email):

    logger = LoggerUtility().get_logger()
    logger.info("**** test_TC_RF_010 STARTED *** ")
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
    rp.enter_email(email)
    rp.enter_phone("9762629797")
    rp.enter_password(ReadConfig.getPassword())
    rp.enter_cpassword(ReadConfig.getPassword())
    rp.click_agree()
    rp.click_continue()
    actual_result = rp.warning_invalidemail()
    expected = "E-Mail Address does not appear to be valid!"

    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(os.path.abspath(os.path.join(os.getcwd(), os.pardir,os.pardir)) + '\\screenshots\\' + 'test_TC_RF_010.png')
        assert False

    logger.info("**** test_TC_RF_010 ENDED ****")