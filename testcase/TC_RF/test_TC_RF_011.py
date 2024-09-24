import os

import pytest

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.logger_utility import LoggerUtility
from utilities.readproperty import ReadConfig


#Validate Registering an Account by providing an invalid phone number
#TC_RF_011


@pytest.mark.parametrize('phone',[("111"),("abcde")])
def test_TC_RF_011(setup,phone):

    logger = LoggerUtility().get_logger()
    logger.info("**** test_TC_RF_011 STARTED *** ")
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
    rp.enter_phone(phone)
    rp.enter_password(ReadConfig.getPassword())
    rp.enter_cpassword(ReadConfig.getPassword())
    rp.click_agree()
    rp.click_continue()
    actual_result = rp.warning_invalidphone()
    expected = "Telephone must be between 3 and 32 characters!"

    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(os.path.abspath(os.path.join(os.getcwd(), os.pardir,os.pardir)) + '\\screenshots\\' + 'test_TC_RF_011.png')
        assert False

    logger.info("**** test_TC_RF_011 ENDED ****")