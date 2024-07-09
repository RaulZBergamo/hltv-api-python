"""
This module provides a helper class to facilitate interaction with the Selenium WebDriver.
It includes methods for initializing the WebDriver and handling repetitive actions.
"""

import logging
import config
from webdriver_manager import chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class SeleniumHelper:
    """
    The SeleniumHelper class provides static methods to simplify the use of Selenium WebDriver.

    Methods:
        get_webdriver() -> webdriver.Chrome:
            Initializes and returns an instance of Chrome WebDriver with predefined options.
        
        wait_for_element() -> None:
            Waits for a specific element to be present on the page within a given timeout period.
    """


    @staticmethod
    def get_webdriver() -> webdriver.Chrome:
        """
        This method returns an instance of Chrome WebDriver with predefined options.

        Returns:
            webdriver.Chrome: An instance of Chrome WebDriver with predefined options.
        """

        logging.info("Initializing WebDriver with Chrome...")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"user-agent={config.USER_AGENT}")

        return webdriver.Chrome(
            service=Service(chrome.ChromeDriverManager().install()),
            options=chrome_options
        )

    @staticmethod
    def wait_for_element(driver: webdriver.Chrome, by: By, value: str, timeout: int = 10) -> None:
        """
        This method waits for a specific element to be present on the page within a given timeout period.

        Args:
            driver (webdriver.Chrome): An instance of Chrome WebDriver.
            by (By): Selenium By object representing the locator strategy.
            value (str): The value of the locator strategy.
            timeout (int, optional): Wait timeout in seconds. Defaults to 10.
        """

        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
