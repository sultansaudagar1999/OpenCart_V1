from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig

# TC_LF_014 Validate the copying of the text entered into the Password field
def test_TC_LF_014(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Navigate to login page
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    # Login page object
    lp = LoginPage(driver)
    lp.enter_password("dummyPassword123")

    # Simulate 'Ctrl + A' and 'Ctrl + C' to copy the password text
    action = ActionChains(driver)
    password_field = lp.get_password_field()

    # Step 1: Select all text in password field
    password_field.send_keys(Keys.CONTROL, 'a')  # Ctrl+A to select all

    # Step 2: Copy text from the field
    password_field.send_keys(Keys.CONTROL, 'c')  # Ctrl+C to copy

    # Step 3: Verify that no text was copied (since it's a password field)
    # Use JavaScript to check if any text was copied to the clipboard
    copied_text = driver.execute_script(
        "return window.getSelection().toString();"
    )
    print("The copied text is",copied_text)
    # Validation: No text should be copied from the password field
    assert copied_text == "", f"Expected no copied text, but got '{copied_text}'"

    # Another approach can be to check if the field is set as a password field:
    field_type = password_field.get_attribute("type")
    assert field_type == "password", f"Expected field type to be 'password', but got '{field_type}'"



