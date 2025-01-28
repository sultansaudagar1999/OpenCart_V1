from selenium.webdriver.common.by import By


class ChangePasswordPage:


    #locators
    password_xpath = "//input[@id='input-password']"
    cpassword_xpath = "//input[@id='input-confirm']"
    continue_button_xpath ="//input[@value='Continue']"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    #actions

    def enter_password(self,password):
        ele = self.driver.find_element(By.XPATH,self.password_xpath)
        ele.clear()
        ele.send_keys(password)

    def enter_confirm_password(self,password):
        ele = self.driver.find_element(By.XPATH,self.cpassword_xpath)
        ele.clear()
        ele.send_keys(password)

    def continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()