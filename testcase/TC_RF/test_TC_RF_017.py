from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities import randomstring
from utilities.readproperty import ReadConfig


# TC_RF_017
# Validate whether the Password fields in the Register Account page are following Password Complexity Standards.

# Testcase Failed When we put low password it should give an error


def test_TC_RF_017(setup):

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
    rp.enter_password("12345")
    rp.enter_cpassword("12345")
    rp.click_agree()
    rp.click_continue()

    actual_result = rp.succes_message()
    expected = "Your Account Has Been Created!"

    if actual_result == expected:
        assert False
    else:
        assert True