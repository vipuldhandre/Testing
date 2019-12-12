from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class AdminLoginLogoutDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path = "E:\webdriver\chromedriver.exe")
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.maximize_window()


    def test_login(self):
        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('admin123')
        #driver.find_element(By.CSS_SELECTOR,'submit-row').click()
        driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
        time.sleep(10)

    def test_logout(self):
        #driver.find_element(By.LINK_TEXT,'Logout')
        driver.find_element_by_xpath('//*[@id="user-tools"]/a[3]').click()
        time.sleep(5)
        

    @classmethod
    def tearDownClass(cls):
        driver.close()

unittest.main()

