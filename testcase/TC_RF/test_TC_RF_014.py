from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig
from selenium.webdriver.common.by import By

def test_TC_RF_014(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Navigate to the register page
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)

    # Define the mandatory fields' labels with their locators
    mandatory_fields_locators = {
        "First Name": (By.XPATH, "//label[@for='input-firstname']//span[@class='text-danger']"),
        "Last Name": (By.XPATH, "//label[@for='input-lastname']//span[@class='text-danger']"),
        "E-Mail": (By.XPATH, "//label[@for='input-email']//span[@class='text-danger']"),
        "Telephone": (By.XPATH, "//label[@for='input-telephone']//span[@class='text-danger']"),
        "Password": (By.XPATH, "//label[@for='input-password']//span[@class='text-danger']"),
        "Password Confirm": (By.XPATH, "//label[@for='input-confirm']//span[@class='text-danger']"),
        "Privacy Policy": (By.XPATH, "//div[@class='form-group required']//input[@name='agree']/following-sibling::label//span[@class='text-danger']")
    }

    # Check for the presence of red * symbol for each mandatory field
    for field, locator in mandatory_fields_locators.items():
        is_present = len(driver.find_elements(*locator)) > 0
        assert is_present, f"Red * symbol is not present next to the {field} field"
