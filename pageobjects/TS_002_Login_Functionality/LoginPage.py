from selenium.webdriver.common.by import By


class LoginPage():

        #Locator
        registerlnk_xpath = "Continue"
        email_xpath = "//input[@id='input-email']"
        password_xpath = "//input[@id='input-password']"
        loginbtn_xpath = "//input[@value='Login']"
        myaccount_xpath = "//*[@id='content']/h2[1]"
        myaccountdrpdown_xpath = "//span[normalize-space()='My Account']"
        logout_lnktxt = "Logout"



        #Constructor

        def __init__(self,driver):
            self.driver = driver

        #Action

        #continue button for register account
        def continue_button(self):
            self.driver.find_element(By.LINK_TEXT,self.registerlnk_xpath).click()

        def enter_email(self,email):
            self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

        def enter_password(self, password):
            self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

        def click_login(self):
            self.driver.find_element(By.XPATH,self.loginbtn_xpath).click()

        def login_button_displaystatus(self):
            return  self.driver.find_element(By.XPATH,self.loginbtn_xpath).is_displayed()

        def myaccount_page(self):
            try:
                self.page = self.driver.find_element(By.XPATH, self.myaccount_xpath).is_displayed()
                return self.page
            except:
                None

        def myaccount_drpdown(self):
            self.driver.find_element(By.XPATH, self.myaccountdrpdown_xpath).click()

        def click_logout(self):
            self.driver.find_element(By.LINK_TEXT, self.logout_lnktxt).click()


