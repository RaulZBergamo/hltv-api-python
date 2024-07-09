"""
This module is used to scrape the HLTV website for matches.

Classes:
    MatchService: A class used to scrape the HLTV website for matches.
"""

import logging
from typing import Any, Dict, List
import config
from selenium.webdriver.common.by import By
from helper.selenium_helper import SeleniumHelper

class MatchService:
    """
    A class used to represent a Match from HLTV

    Attributes
    ----------

    driver : webdriver.Chrome
        The WebDriver used to scrape the HLTV website

    """

    def __init__(self) -> None:
        self.__init_webdriver()

    def __init_webdriver(self) -> None:
        self.driver = SeleniumHelper.get_webdriver()

    def get_matches(self) -> List[Dict[str, Any]]:
        """
        This method is used to get the matches from HLTV.

        Returns:
            List[Dict[str, Any]]: A list of matches from
            HLTV in the form of a dictionary.
        """
        logging.info("Getting matches from HLTV...")

        self.driver.get(f"{config.CONFIG['BASE_URL']}/{config.CONFIG['MATCHES']}")

        SeleniumHelper.wait_for_element(
            self.driver,
            By.XPATH,
            "//div[contains(text(), 'All matches')]"
        )

        return []

    def __del__(self) -> None:
        self.driver.quit()
