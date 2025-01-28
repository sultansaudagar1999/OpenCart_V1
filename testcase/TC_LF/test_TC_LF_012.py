from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities import randomstring
from utilities.readproperty import ReadConfig

# TC_LF_012
# Validate the number of unsucessful login attemps

def test_TC_LF_012(setup):

    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()

    lg = LoginPage(driver)
    max_attempt = 6
    user_email = randomstring.random_string_generator() + '@gmail.com'
    user_pass =  ReadConfig.getPassword()

    for attempt in range(1 , max_attempt+1):
        lg.enter_email(user_email)
        lg.enter_password(user_pass)
        lg.click_login()


        if attempt == max_attempt:
            act_message = lg.warning_incorrect_details()
            exp_message = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
            assert act_message == exp_message,f"Expected: '{exp_message}', but got '{act_message}'"
        else:
            act_message1 = lg.warning_incorrect_details()
            exp_message1 = "Warning: No match for E-Mail Address and/or Password."
            assert act_message1 == exp_message1,f"Expected: '{exp_message1}', but got '{act_message1}'"
        lg.clear_email()
        lg.clear_password()