# src/with_selenium_manager.py
from selenium import webdriver

# Pinned Chrome major version.
BROWSER_VERSION = "155"

options = webdriver.ChromeOptions()
options.browser_version = BROWSER_VERSION

driver = webdriver.Chrome(options=options)
print(f"Browser: {driver.capabilities['browserVersion']}")
print(f"Driver: {driver.capabilities['chrome']['chromedriverVersion'].split()[0]}")
