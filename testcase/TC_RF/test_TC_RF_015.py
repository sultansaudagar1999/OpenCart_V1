import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.readproperty import ReadConfig


# TC_RF_015
# Validate the details that are provided while Registering an Account are stored in the Database

def test_TC_RF_015(setup):

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
    rp.click_agree()
    rp.click_continue()
    actual_result = rp.succes_message()
    expected = "Your Account Has Been Created!"

    print(actual_result)
    time.sleep(2)

    if actual_result == expected:
        assert True
    else:
        driver.save_screenshot(os.path.abspath(os.path.join(os.getcwd(), os.pardir,os.pardir)) + '\\screenshots\\' + 'test_TC_RF_015.png')
        assert False

