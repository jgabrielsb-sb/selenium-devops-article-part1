# src/without_selenium_manager.py
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to the chromedriver we downloaded by hand (".exe" on Windows).
CHROMEDRIVER_PATH = Path("drivers/chromedriver")

options = webdriver.ChromeOptions()
service = Service(executable_path=str(CHROMEDRIVER_PATH))

driver = webdriver.Chrome(service=service, options=options)
