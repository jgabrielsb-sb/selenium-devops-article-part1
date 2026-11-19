# src/automations/application/base_selenium_automation.py
import time
from abc import ABC, abstractmethod
from pathlib import Path

from selenium.webdriver.common.by import By

from automations.infra.selenium.webdrivers.webdriver_session import WebdriverSession


class BaseSeleniumAutomation(ABC):
    """
    Interface to represent selenium automations.

    Child classes implement only the steps of the automation in `_run()`.
    `run()` opens the session before those steps and closes it afterwards,
    so no automation has to deal with starting or quitting the browser.
    """

    def __init__(self, session: WebdriverSession):
        self._session = session

    def run(self):
        with self._session:
            return self._run()

    @abstractmethod
    def _run(self):
        raise NotImplementedError()


class DownloadFileFromSeleniumWebsite(BaseSeleniumAutomation):
    """
    An automation that goes to the selenium website and downloads a file.
    """

    SOURCE_URL = "https://www.selenium.dev/selenium/web/downloads/download.html"
    FILE_NAME = "file_1.txt"
    TIMEOUT_SECONDS = 30

    def _run(self) -> Path:
        driver = self._session.driver
        file_path = self._session.download_dir / self.FILE_NAME
        # If the file is already there, Chrome saves the new one as "file_1 (1).txt"
        # and the wait below would succeed on the old file. Remove it first.
        file_path.unlink(missing_ok=True)

        driver.get(self.SOURCE_URL)
        driver.find_element(By.CSS_SELECTOR, f"a[href='{self.FILE_NAME}']").click()
        self._wait_for_download(file_path)
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
