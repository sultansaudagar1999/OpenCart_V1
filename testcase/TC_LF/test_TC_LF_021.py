from pageobjects.TS_001_Register_Functionality.HomePage import HomePage
from pageobjects.TS_002_Login_Functionality.LoginPage import LoginPage
from utilities.readproperty import ReadConfig


# TC_LF_021
# Validate the breadcrumb, Page Heading, Page Title and Page URL of Login page


def test_TC_LF_021(setup):
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()

    hp = HomePage(driver)
    hp.click_myaccount()
    hp.click_login()
    act_list = []
    lp = LoginPage(driver)
    breadcrumb = lp.get_breadcumb()
    act_list.append(breadcrumb)
    page_heading = lp.get_pageheading()
    act_list.append(page_heading)
    page_title = driver.title
    act_list.append(page_title)
    page_url = driver.current_url
    act_list.append(page_url)


    exp_list = ["Account Login","New Customer","Account Login","https://naveenautomationlabs.com/opencart/index.php?route=account/login"]

    ind = 0
    for i in act_list:
        if i == exp_list[ind]:
            assert True
        else:
            assert False
        ind +=1

