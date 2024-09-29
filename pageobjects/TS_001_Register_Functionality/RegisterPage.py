from selenium.webdriver.common.by import By


class RegisterPage:
    # Locator
    breadcrumb_css = "ul.breadcrumb"
    page_heading_css = "h1"
    first_xpath = "//input[@id='input-firstname']"
    last_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    phone_xpath = "//input[@id='input-telephone']"
    pass_xpath = "//input[@id='input-password']"
    cpass_xpath = "//input[@id='input-confirm']"
    agree_xpath = "//input[@name='agree']"
    conti_xpath = "//input[@value='Continue']"
    login_link_xpath = "//*[@id='column-right']/div/a[1]"
    success_xpath = "//*[@id='content']/h1"
    firstname_warning_xpath = "//*[@id='account']/div[2]/div/div"
    lastname_warning_xpath = "//*[@id='account']/div[3]/div/div"
    email_warning_xpath = "//*[@id='account']/div[4]/div/div"
    phone_warning_xpath = "//*[@id='account']/div[5]/div/div"
    password_warning_xpath = "//*[@id='content']/form/fieldset[2]/div[1]/div/div"
    password_mismatcherror_xpath = "//*[@id='content']/form/fieldset[2]/div[2]/div/div"
    tcwarning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    subscribeyes_xpath = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    subscribeno_xpath = "//input[@value='0']"
    continuesucces_btn_xpath = "//a[@class='btn btn-primary']"
    subsribelink_xpath = "//*[@id='content']/ul[4]/li/a"
    registerpage_xpath = "//*[@id='content']/h1"
    already_reg_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_placeholder_id = "input-firstname"
    lastname_placeholder_id = "input-lastname"
    email_placeholder_id = "input-email"
    telephone_placeholder_id = "input-telephone"
    password_placeholder_id = "input-password"
    confirm_placeholder_id = "input-confirm"
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action
    def register_page(self):
        try:
            self.page = self.driver.find_element(By.XPATH,self.registerpage_xpath)
            return self.page.text
        except:
            None
    def get_breadcrumb(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.breadcrumb_css).text

    def get_page_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_heading_css).text

    def enter_firstname(self,firstname):
        self.driver.find_element(By.XPATH, self.first_xpath).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.XPATH, self.last_xpath).send_keys(lastname)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(phone)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.pass_xpath).send_keys(password)

    def enter_cpassword(self,password):
        self.driver.find_element(By.XPATH, self.cpass_xpath).send_keys(password)

    def password_field_type(self):
        return self.driver.find_element(By.XPATH, self.pass_xpath).get_attribute("type")

    def cpassword_field_type(self):
        return self.driver.find_element(By.XPATH, self.cpass_xpath).get_attribute("type")

    def clicklogin_link_registerpage(self):
        self.driver.find_element(By.XPATH,self.login_link_xpath).click()

    def password_mismatch(self):
        try:
            self.error = self.driver.find_element(By.XPATH, self.password_mismatcherror_xpath)
            return self.error.text
        except:
            None

    def already_registered(self):
        try:
            self.alert = self.driver.find_element(By.XPATH, self.already_reg_xpath)
            return self.alert.text
        except:
            None

    def click_agree(self):
        self.driver.find_element(By.XPATH, self.agree_xpath).click()

    def privacy_agree_status(self):
        self.status = self.driver.find_element(By.XPATH, self.agree_xpath).is_selected()
        return self.status

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.conti_xpath).click()

    def firstname_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID,self.firstname_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def lastname_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID,self.lastname_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def email_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID,self.email_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def telephone_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID,self.telephone_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def password_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID,self.password_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def confirmpwd_placeholder(self):
        self.name_placeholder = self.driver.find_element(By.ID, self.confirm_placeholder_id).get_attribute("placeholder")
        return self.name_placeholder

    def succes_message(self):
        try:
            self.succes = self.driver.find_element(By.XPATH,self.success_xpath)
            return self.succes.text
        except:
            None

    def warning_invalidfirstname(self):
        try:
            self.invalidfirstname = self.driver.find_element(By.XPATH,self.firstname_warning_xpath)
            return self.invalidfirstname.text
        except:
            None

    def warning_invalidlastname(self):
        try:
            self.invalidlastname = self.driver.find_element(By.XPATH,self.lastname_warning_xpath)
            return self.invalidlastname.text
        except:
            None

    def warning_invalidemail(self):
        try:
            self.invalidemail = self.driver.find_element(By.XPATH,self.email_warning_xpath)
            return self.invalidemail.text
        except:
            None

    def warning_invalidphone(self):
        try:
            self.invalidphone = self.driver.find_element(By.XPATH,self.phone_warning_xpath)
            return self.invalidphone.text
        except:
            None

    def warning_invalidpassword(self):
        try:
            self.invalidpassword = self.driver.find_element(By.XPATH, self.password_warning_xpath)
            return self.invalidpassword.text
        except:
            None

    def warning_tcaccept(self):
        try:
            self.warning = self.driver.find_element(By.XPATH,self.tcwarning_xpath)
            return self.warning.text
        except:
            None
    def subscribe_yes(self):
        self.yes = self.driver.find_element(By.XPATH,self.subscribeyes_xpath)
        return self.yes

    def subscribe_no(self):
        self.no = self.driver.find_element(By.XPATH,self.subscribeno_xpath)
        return self.no

    def continue_btnsucces(self):
        self.driver.find_element(By.XPATH,self.continuesucces_btn_xpath).click()

    def subscribe_option(self):
        try:
            self.subscribe = self.driver.find_element(By.XPATH,self.subsribelink_xpath)
            return self.subscribe.text
        except:
            None







