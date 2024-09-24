import os
import time

from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from testcase.TC_RF.conftest import setup
from utilities import excel_utility
from utilities.excel_utility import getRowCount, getColumnCount
from utilities.logger_utility import LoggerUtility
from utilities.readproperty import ReadConfig



def test_DataDriven_Login(setup):
    logger = LoggerUtility().get_logger()
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir)) + "\\testdata\\Opencart_LoginData.xlsx"
    lst_status = []
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.implicitly_wait(5)
    driver.maximize_window()
    rows = getRowCount(path,"Sheet1")
    coloums = getColumnCount(path,"Sheet1")

    hp = HomePage(driver)
    lp = LoginPage(driver)

    for r in range(2, rows + 1):
            hp.click_myaccount()
            hp.click_login()
            email = excel_utility.readData(path, "Sheet1", r, 1)
            password = excel_utility.readData(path, "Sheet1", r, 2)
            exp = excel_utility.readData(path, "Sheet1", r, 3)
            lp.enter_email(email)
            lp.enter_password(password)
            lp.click_login()
            time.sleep(3)
            targetpage = lp.myaccount_page()


            if exp == 'Valid':
                if targetpage == True:
                    lst_status.append('Pass')
                    lp.click_logout()
                else:
                    lst_status.append('Fail')
            elif exp == 'Invalid':
                if targetpage == True:
                    lst_status.append('Fail')
                    lp.click_logout()
                else:
                    lst_status.append('Pass')
    driver.close()
    # final validation
    if "Fail" not in lst_status:
        assert True
    else:
        assert False
    logger.info("******* End of test_DataDriven_Login **********")


