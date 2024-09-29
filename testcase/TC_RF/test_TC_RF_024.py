from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.readproperty import ReadConfig


# TC_RF_024
# Validate Registring an Account, by filling 'Password' field and not filling 'Password Confirm' field

def test_TC_RF_024(setup):

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
    rp.click_agree()
    rp.click_continue()

    act_error = rp.password_mismatch()
    exp_error = "Password confirmation does not match password!"

    if act_error == exp_error:
        assert True
    else:
        assert False