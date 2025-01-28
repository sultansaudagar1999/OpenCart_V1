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
        forgot_password_lnk = "Forgotten Password"
        register_lnk = "Register"
        warning_css = "body:nth-child(2) div.container:nth-child(4) > div.alert.alert-danger.alert-dismissible"
        change_your_password_lnk = "Change your password"
        new_customer_continue_btn = "Continue"
        register_page_xpath = "//*[@id='content']/h1"
        breadcumb_xpath = "//*[@id='account-login']/ul"
        page_heading_css = "h2"



        #Constructor

        def __init__(self,driver):
            self.driver = driver

        #Action

        #continue button for register account
        def continue_button(self):
            self.driver.find_element(By.LINK_TEXT,self.registerlnk_xpath).click()

        def enter_email(self,email):
            ele = self.driver.find_element(By.XPATH,self.email_xpath)
            ele.clear()
            ele.send_keys(email)

        def enter_password(self, password):
            ele = self.driver.find_element(By.XPATH, self.password_xpath)
            ele.clear()
            ele.send_keys(password)

        def clear_email(self):
            self.driver.find_element(By.XPATH,self.email_xpath).clear()

        def clear_password(self):
            self.driver.find_element(By.XPATH, self.password_xpath).clear()

        def email_placeholder(self):
            return self.driver.find_element(By.XPATH,self.email_xpath).get_attribute("placeholder")

        def password_placeholder(self):
            return self.driver.find_element(By.XPATH, self.password_xpath).get_attribute("placeholder")

        def click_login(self):
            self.driver.find_element(By.XPATH,self.loginbtn_xpath).click()

        def login_button_displaystatus(self):
            return  self.driver.find_element(By.XPATH,self.loginbtn_xpath).is_displayed()

        def myaccount_page(self):
            try:
                self.page = self.driver.find_element(By.XPATH, self.myaccount_xpath).is_displayed()
                return self.page
            except:
                return False

        def myaccount_drpdown(self):
            self.driver.find_element(By.XPATH, self.myaccountdrpdown_xpath).click()

        def click_logout(self):
            self.driver.find_element(By.LINK_TEXT, self.logout_lnktxt).click()

        def is_logout_present(self):
            return len(self.driver.find_elements(By.LINK_TEXT,self.logout_lnktxt)) > 0

        def click_forgot_password(self):
            self.driver.find_element(By.LINK_TEXT,self.forgot_password_lnk).click()

        def click_register(self):
            self.driver.find_element(By.LINK_TEXT,self.register_lnk).click()

        def register_page_status(self):
            return self.driver.find_element(By.XPATH,self.register_page_xpath).is_displayed()

        def warning_incorrect_details(self):
            return self.driver.find_element(By.CSS_SELECTOR, self.warning_css).text

        def password_box_type(self):
            return self.driver.find_element(By.XPATH,self.password_xpath).get_attribute("type")

        def get_password_field(self):
            return self.driver.find_element(By.XPATH, self.password_xpath)

        def change_your_password(self):
            self.driver.find_element(By.LINK_TEXT,self.change_your_password_lnk).click()

        def newcustomer_continue(self):
            self.driver.find_element(By.LINK_TEXT,self.new_customer_continue_btn).click()

        def get_breadcumb(self):
            return self.driver.find_element(By.XPATH,self.breadcumb_xpath).text

        def get_pageheading(self):
            return self.driver.find_element(By.CSS_SELECTOR,self.page_heading_css).text





