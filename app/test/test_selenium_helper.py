import sys

sys.path.append("./app/")

import unittest
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from helper.selenium_helper import SeleniumHelper

class SeleniumHelperTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(chrome.ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_get_webdriver(self):
        driver = SeleniumHelper.get_webdriver()
        self.assertIsInstance(driver, webdriver.Chrome)

    def test_wait_for_element(self):
        element = (By.XPATH, "//h1[contains(text(), 'Example Domain')]")
        self.driver.get("https://example.com")
        SeleniumHelper.wait_for_element(self.driver, *element)
        self.assertTrue(EC.presence_of_element_located(element))

if __name__ == '__main__':
    unittest.main()
