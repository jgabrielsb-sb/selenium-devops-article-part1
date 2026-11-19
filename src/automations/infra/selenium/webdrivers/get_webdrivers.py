# src/automations/infra/selenium/webdrivers/get_webdrivers.py
from pathlib import Path

from selenium import webdriver


def get_chrome_webdriver(download_dir: Path) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(download_dir),
            "download.prompt_for_download": False,
        },
    )
    return webdriver.Chrome(options=options)
