from selenium.webdriver.common.by import By


class HomePage():

        #Locator
        myaccount_xpath = "//*[@id='top-links']/ul/li[2]/a/span[2]"
        register_linktxt = "Register"

        #Constructor

        def __init__(self,driver):
            self.driver = driver

        #Action
        def click_myaccount(self):
            self.driver.find_element(By.XPATH,self.myaccount_xpath).click()

        def click_register(self):
            self.driver.find_element(By.LINK_TEXT, self.register_linktxt).click()
