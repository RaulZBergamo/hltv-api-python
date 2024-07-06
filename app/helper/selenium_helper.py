import logging
import config
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class SeleniumHelper:

    @staticmethod
    def get_webdriver() -> webdriver.Chrome:
        logging.info("Initializing WebDriver with Chrome...")

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"user-agent={config.USER_AGENT}")

        return webdriver.Chrome(service=Service(chrome.ChromeDriverManager().install()), options=chrome_options)

    @staticmethod
    def wait_for_element(driver: webdriver.Chrome, by: By, value: str, timeout: int = 10) -> None:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))