from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import continue_request


class LogoutPage:


    logout_page_xpath = "//*[@id='content']/h1"
    continue_button_lnktxt = "Continue"


    def __init__(self,driver):
        self.driver = driver


    #Action

    def verify_logoutpage(self):
        return  self.driver.find_element(By.XPATH,self.logout_page_xpath).text

    def logoutpage_continue_button(self):
        self.driver.find_element(By.LINK_TEXT,self.continue_button_lnktxt).click()