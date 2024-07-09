import sys

sys.path.append("./app/")

import unittest
from selenium import webdriver
from unittest.mock import patch
from services.match_service import MatchService

class TestMatchService(unittest.TestCase):

    @patch('services.match_service.SeleniumHelper')
    def test_get_matches(self, mock_selenium_helper):
        # Mock the WebDriver instance
        mock_driver = webdriver.Chrome()
        mock_selenium_helper.get_webdriver.return_value = mock_driver

        # Create an instance of MatchService
        match_service = MatchService()

        # Call the get_matches method
        result = match_service.get_matches()

        # Assert the expected result
        self.assertEqual(result, (None, None, None))

if __name__ == '__main__':
    unittest.main()