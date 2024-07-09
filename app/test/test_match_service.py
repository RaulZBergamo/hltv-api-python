"""
Test the MatchService class
"""

import unittest
from unittest.mock import patch
from services.match_service import MatchService
from helper.selenium_helper import SeleniumHelper

class TestMatchService(unittest.TestCase):
    """
    Classe to test the MatchService class
    """

    def setUp(self):
        self.driver = SeleniumHelper().get_webdriver()

    @patch('services.match_service.SeleniumHelper')
    def test_get_matches(self, mock_selenium_helper):
        """
        Tests the get_matches method of the MatchService class
        """

        # Mock the WebDriver instance
        mock_driver = self.driver
        mock_selenium_helper.get_webdriver.return_value = mock_driver

        # Create an instance of MatchService
        match_service = MatchService()

        # Call the get_matches method
        result = match_service.get_matches()

        # Assert the expected result
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
