# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
#
# driver.get("https://naveenautomationlabs.com/opencart/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/a/span[2]").click()
# driver.find_element(By.LINK_TEXT,"Register").click()
#
# driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("sultan")
# driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("saudagar")
# driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("abw12@gmail.com")
# driver.find_element(By.XPATH,"//input[@id='input-telephone']").send_keys("7878454580")
# driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("123456")
# driver.find_element(By.XPATH,"//input[@id='input-confirm']").send_keys("123456")
# driver.find_element(By.XPATH,"//input[@name='agree']").click()
# driver.find_element(By.XPATH,"//input[@value='Continue']").click()
#
# succes  = driver.find_element(By.XPATH,"//*[@id='content']/h1")
#
# print(succes.text)
#
#
# time.sleep(5)
#
