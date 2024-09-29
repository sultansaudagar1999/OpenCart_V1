from tarfile import REGULAR_TYPES

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


# TC_RF_022
# Validate the Password text entered into the 'Password' and 'Password Confirm' field of 'Register Account' functionality is toggled to hide its visibility

def test_TC_RF_022(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)
    rp.enter_password("123456")
    rp.enter_cpassword("123456")

    password_field_type = rp.password_field_type()
    confirm_password_field_type = rp.cpassword_field_type()

    assert password_field_type == "password","Not password field type"
    assert confirm_password_field_type == "password","Not a password field type"
