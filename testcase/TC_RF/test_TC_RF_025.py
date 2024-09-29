
from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_001_Register_Functionality.RegisterPage import RegisterPage
from utilities.readproperty import ReadConfig


# TC_RF_025 Validate Breadcrumb, Page Heading, Page URL, and Page Title of Register Account Page

def test_TC_RF_025(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Navigate to the register page
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_register()

    rp = RegisterPage(driver)

    # Validate Breadcrumb
    expected_breadcrumb = "Account Register"
    actual_breadcrumb = rp.get_breadcrumb()
    assert expected_breadcrumb in actual_breadcrumb, f"Expected breadcrumb: {expected_breadcrumb}, but got {actual_breadcrumb}"

    # Validate Page Heading
    expected_heading = "Register Account"
    actual_heading = rp.get_page_heading()
    assert actual_heading == expected_heading, f"Expected heading: {expected_heading}, but got {actual_heading}"

    # Validate Page URL
    expected_url = "https://naveenautomationlabs.com/opencart/index.php?route=account/register"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got {actual_url}"

    # Validate Page Title
    expected_title = "Register Account"
    actual_title = driver.title
    assert actual_title == expected_title, f"Expected title: {expected_title}, but got {actual_title}"
