# src/automations/infra/selenium/webdrivers/get_webdrivers.py
import tempfile
from pathlib import Path

from selenium import webdriver


def set_download_default_dir(download_dir: Path) -> Path:
    """
    Make sure `download_dir` can be used as Chrome's download directory.

    Chrome does not raise any error when the download directory is invalid: it
    silently saves the file somewhere else (or nowhere). So we validate the
    directory ourselves and fail fast, before the browser is even opened.
    """
    if not isinstance(download_dir, Path):
        raise TypeError(f"download_dir must be a Path, got {type(download_dir).__name__}")

    # A relative path depends on the folder the script is started from, and
    # Chrome ignores it anyway. Only absolute paths are accepted.
    if not download_dir.is_absolute():
        raise ValueError(f"download_dir must be an absolute path, got '{download_dir}'")

    # Create the directory (and its parents) if it does not exist yet.
    download_dir.mkdir(parents=True, exist_ok=True)

    # Check that the current user can actually write there by creating
    # (and automatically removing) a temporary file inside it.
    try:
        with tempfile.TemporaryFile(dir=download_dir):
            pass
    except OSError as error:
        raise PermissionError(f"download_dir '{download_dir}' is not writable") from error

    return download_dir


def get_chrome_webdriver(download_dir: Path) -> webdriver.Chrome:
    # Validates the directory; if anything is wrong, raises an exception here
    # instead of failing silently in the middle of the automation.
    download_dir = set_download_default_dir(download_dir)

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(download_dir),
            "download.prompt_for_download": False,
        },
    )
    return webdriver.Chrome(options=options)
