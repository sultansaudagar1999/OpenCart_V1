from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


# TC_RF_013 Validate all the fields in the Register Account page have the proper placeholders

def test_TC_RF_013(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Navigate to the register page
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)

    # Define expected placeholders
    expected_placeholders = {
        "First Name": rp.firstname_placeholder(),
        "Last Name": rp.lastname_placeholder(),
        "E-Mail": rp.email_placeholder(),
        "Telephone": rp.telephone_placeholder(),
        "Password": rp.password_placeholder(),
        "Password Confirm": rp.confirmpwd_placeholder(),
    }

    # Assert each placeholder
    for field, actual_placeholder in expected_placeholders.items():
        assert actual_placeholder == field, f"Expected placeholder: '{field}', but got: '{actual_placeholder}'"
