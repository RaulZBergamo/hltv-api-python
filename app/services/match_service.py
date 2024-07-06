import logging
import config
from models.match import Match
from typing import Any
from selenium.webdriver.common.by import By
from helper.selenium_helper import SeleniumHelper


class MatchService:
    """
    A class used to represent a Match from HLTV

    Attributes
    ----------

    driver : webdriver.Chrome
        The WebDriver used to scrape the HLTV website

    Match : Match 
        The object that represents a Match from HLTV

    """

    def __init__(self) -> None:
        self.__init_webdriver()

    def __init_webdriver(self) -> None:
        self.driver = SeleniumHelper.get_webdriver()

    def get_matches(self) -> tuple[dict[str, Any], int, dict[str, str]]:
        logging.info("Getting matches from HLTV...")

        self.driver.get(f"{config.CONFIG['BASE_URL']}/{config.CONFIG['MATCHES']}")

        SeleniumHelper.wait_for_element(self.driver, By.XPATH, "//div[contains(text(), 'All matches')]")

        print()
        