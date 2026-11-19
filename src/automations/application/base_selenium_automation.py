# src/automations/application/base_selenium_automation.py
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By


class BaseSeleniumAutomation(ABC):
    """
    Interface to represent selenium automations
    """

    def __init__(self, webdriver):
        self._webdriver = webdriver

    @abstractmethod
    def run(self):
        raise NotImplementedError()


class DownloadFileFromSeleniumWebsite(BaseSeleniumAutomation):
    """
    An automation that goes to the selenium website and downloads a file.
    """

    SOURCE_URL = "https://www.selenium.dev/selenium/web/downloads/download.html"
    FILE_NAME = "file_1.txt"

    def run(self):
        try:
            self._webdriver.get(self.SOURCE_URL)
            self._webdriver.find_element(By.CSS_SELECTOR, f"a[href='{self.FILE_NAME}']").click()
        finally:
            self._webdriver.quit()
