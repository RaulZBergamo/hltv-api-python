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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(chrome.ChromeDriverManager().install()), 
            options=chrome_options
        )
        
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
