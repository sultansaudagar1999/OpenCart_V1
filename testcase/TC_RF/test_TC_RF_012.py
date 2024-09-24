import os
import time
from argparse import Action

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.logger_utility import LoggerUtility
from utilities.readproperty import ReadConfig


# Validate Registering an Account by using the Keyboard keys
#TC_RF_012



def test_TC_RF_012(setup):


    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    rp.enter_firstname("Sultan")
    act = ActionChains(driver)
    act.key_down(Keys.TAB).send_keys("Saudagar").key_up(Keys.TAB).perform()
    email = randomstring.random_string_generator() + '@gmail.com'
    act.key_down(Keys.TAB).send_keys(email).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).send_keys("9762628372").key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).send_keys(ReadConfig.getPassword()).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).send_keys(ReadConfig.getPassword()).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    act.key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


    actual_result = rp.succes_message()
    expected = "Your Account Has Been Created!"

    print(actual_result)
    time.sleep(5)

    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_012.png')
        assert False


