# src/main.py
from automations.application.base_selenium_automation import DownloadFileFromSeleniumWebsite
from automations.infra.selenium.webdrivers.webdriver_session import WebdriverSession
from automations.settings import DOWNLOAD_DIR

if __name__ == "__main__":
    # 1. configuration: comes from settings (and environment variables)
    session = WebdriverSession(download_dir=DOWNLOAD_DIR)

    # 2. automation: receives the session; it does not create or close the browser
    automation = DownloadFileFromSeleniumWebsite(session=session)

    # 3. execution: run() opens the session, runs the steps and closes it
    file_path = automation.run()
    print(f"Downloaded {file_path} ({file_path.stat().st_size} bytes)")
