import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage

from utilities import randomstring
from utilities.readproperty import ReadConfig


# Validate Registering an Account by providing all the fields
# TC_RF_004

def test_TC_RF_004(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    rp.click_continue()

    actual_result = rp.warning_invalidfirstname()
    expected = "First Name must be between 1 and 32 characters!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(os.path.abspath(os.path.join(os.getcwd(), os.pardir,os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

    actual_result = rp.warning_invalidlastname()
    expected = "Last Name must be between 1 and 32 characters!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

    actual_result = rp.warning_invalidemail()
    expected = "E-Mail Address does not appear to be valid!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

    actual_result = rp.warning_invalidphone()
    expected = "Telephone must be between 3 and 32 characters!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

    actual_result = rp.warning_invalidpassword()
    expected = "Password must be between 4 and 20 characters!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

    actual_result = rp.warning_tcaccept()
    expected = "Warning: You must agree to the Privacy Policy!"
    print(actual_result)
    time.sleep(2)
    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(
            os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + '\\screenshots\\' + 'test_TC_RF_004.png')
        assert False

