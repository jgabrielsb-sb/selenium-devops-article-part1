# src/main.py
from pathlib import Path

from automations.application.base_selenium_automation import DownloadFileFromSeleniumWebsite
from automations.infra.selenium.webdrivers.get_webdrivers import get_chrome_webdriver

DOWNLOAD_DIR = Path("media")

if __name__ == "__main__":
    driver = get_chrome_webdriver(DOWNLOAD_DIR)
    DownloadFileFromSeleniumWebsite(webdriver=driver).run()
