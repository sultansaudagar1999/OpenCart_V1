from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    # Locator
    ipt_email_xpath = "//*[@id='input-email']"
    forgot_password_status_xpath = "//*[@id='content']/h1"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action
    def email_box_status(self):
            return self.driver.find_element(By.XPATH,self.ipt_email_xpath).is_displayed()

    def enter_email_forgotpassword(self,email):
            self.driver.find_element(By.XPATH, self.ipt_email_xpath).send_keys(email)

    def forgot_page_status(self):
            return self.driver.find_element(By.XPATH,self.forgot_password_status_xpath).is_displayed()


