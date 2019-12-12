##from selenium import webdriver
##driver = webdriver.Chrome(executable_path = "E:\webdriver\chromedriver.exe")
##driver.get("https://www.linkedin.com/")
##driver.maximize_window()
##print("Title of web page:",driver.title)
##print("Currentpage URL:",driver.current_url)
##driver.get("https://www.facebook.com/")
##print("Title of web page:",driver.title)
##print("Currentpage URL:",driver.current_url)
##driver.back()
##print("After back current url:",driver.current_url)
##driver.forward()
##print("After forward current url:",driver.current_url)
##driver.close()

'''
how to locate web elements:
----------------------------
driver.find_element_by_id('id')
driver.find_element_by_name('name')
driver.find_element_by_xpath('path')
driver.find_element_by_css_selector('css')
driver.find_element_by_link_text('text')


more convenient method
----------------------
driver.find_element(By.ID,'id')
driver.find_element(By.Name,'name')
driver.find_element(By.LINK_TEXT,'txt')
driver.find_element(By.CSS_SELECTOR,'css')

'''

'''
Write a python Testscript to test Google Search Functionality by using selenium unittesting?
'''
##from selenium import webdriver
##import unittest
##import time
##
##
##class GoogleSearchDemo(unittest.TestCase):
##    def setUp(self):
##        global driver
##        driver = webdriver.Chrome(executable_path = "E:\webdriver\chromedriver.exe")
##        driver.get("https://www.google.com/")
##        driver.maximize_window()
##
##    def test(self):
##        driver.find_element_by_name('q').send_keys('Virat Kohli')
##        time.sleep(5)
##        driver.find_element_by_name('btnK').click()
##        time.sleep(5)
##        driver.find_element_by_class_name('LC20lb').click()
##        time.sleep(10)
##
##    def tearDown(self):
##        driver.close()
##
##unittest.main()        
        
'''
Testing HMS Login and Logout Functionality by using Unit Test Framework and selenium.
--------------------------

class setUpClass()
class tearDownClass()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class HMSLoginLogoutDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path="E:\webdriver\chromedriver.exe")
        driver.get("http://www.seleniumbymahesh.com/")
        driver.maximize_window()

    def test_login(self):
        driver.find_element(By.LINK_TEXT,'HMS').click()
        time.sleep(10)
        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('admin')
        driver.find_element(By.NAME,'submit').click()
        time.sleep(5)

    def test_logout(self):
        driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        driver.close()

unittest.main()
    




































































