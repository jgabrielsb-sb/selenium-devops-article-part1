# src/automations/application/base_selenium_automation.py
import time
from abc import ABC, abstractmethod
from pathlib import Path

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
    TIMEOUT_SECONDS = 30

    def __init__(self, webdriver, download_dir: Path):
        super().__init__(webdriver)
        self._download_dir = download_dir

    def run(self) -> Path:
        file_path = self._download_dir / self.FILE_NAME
        # If the file is already there, Chrome saves the new one as "file_1 (1).txt"
        # and the wait below would succeed on the old file. Remove it first.
        file_path.unlink(missing_ok=True)

        try:
            self._webdriver.get(self.SOURCE_URL)
            self._webdriver.find_element(By.CSS_SELECTOR, f"a[href='{self.FILE_NAME}']").click()
            self._wait_for_download(file_path)
        finally:
            self._webdriver.quit()

        return file_path

    def _wait_for_download(self, file_path: Path) -> None:
        """Chrome writes to '<name>.crdownload' and renames it to '<name>' when the download finishes."""
        deadline = time.monotonic() + self.TIMEOUT_SECONDS
        while not file_path.exists():
            if time.monotonic() > deadline:
                raise TimeoutError(
                    f"{file_path.name} was not downloaded to {file_path.parent} "
                    f"in {self.TIMEOUT_SECONDS} seconds"
                )
            time.sleep(0.5)
