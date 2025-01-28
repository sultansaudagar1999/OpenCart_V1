import time
from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig

def test_TC_LG_003(setup):
    # Step 1: Open the browser and navigate to the application
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Step 2: Perform login
    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    lg.enter_email(ReadConfig.getUseremail())
    lg.enter_password(ReadConfig.getPassword())
    lg.click_login()
    print(driver.title)

    # Step 3: Verify the login was successful
    assert driver.title == "My Account", "Login failed or incorrect page loaded"
    print("Step 3: User logged in successfully.")

    # Step 4: Save cookies and close the browser without logging out
    cookies = driver.get_cookies()
    driver.quit()

    # Step 5: Reopen the browser and navigate to the application
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)

    # Step 6: Restore cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    # Step 7: Verify the user session is retained
    assert driver.title == "My Account", "User session not retained after closing the browser"
    print("Step 7: User session retained successfully.")

    # Close the browser
    driver.quit()
