# src/main.py
from automations.application.base_selenium_automation import DownloadFileFromSeleniumWebsite
from automations.infra.selenium.webdrivers.get_webdrivers import get_chrome_webdriver
from automations.settings import DOWNLOAD_DIR

if __name__ == "__main__":
    driver = get_chrome_webdriver(DOWNLOAD_DIR)
    file_path = DownloadFileFromSeleniumWebsite(webdriver=driver, download_dir=DOWNLOAD_DIR).run()
    print(f"Downloaded {file_path} ({file_path.stat().st_size} bytes)")
