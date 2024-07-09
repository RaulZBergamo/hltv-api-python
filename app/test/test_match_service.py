import sys

sys.path.append("./app/")

import unittest
from selenium import webdriver
from unittest.mock import patch
from services.match_service import MatchService
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome

class TestMatchService(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(chrome.ChromeDriverManager().install()), 
            options=chrome_options
        )

    @patch('services.match_service.SeleniumHelper')
    def test_get_matches(self, mock_selenium_helper):
        # Mock the WebDriver instance
        mock_driver = self.driver
        mock_selenium_helper.get_webdriver.return_value = mock_driver

        # Create an instance of MatchService
        match_service = MatchService()

        # Call the get_matches method
        result = match_service.get_matches()

        # Assert the expected result
        self.assertEqual(result, (None, None, None))

if __name__ == '__main__':
    unittest.main()
