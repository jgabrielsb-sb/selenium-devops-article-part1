# src/automations/infra/selenium/webdrivers/webdriver_session.py
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from .get_webdrivers import get_chrome_webdriver


class WebdriverSessionAlreadyOpenException(Exception):
    pass


class WebdriverSessionNotOpenException(Exception):
    pass


class WebdriverSession:
    """
    Owns the lifecycle of one webdriver: it creates the browser, gives access to
    it while it is open, and guarantees that it is closed at the end.

    Use it as a context manager, so the browser is closed even if the code
    inside the block raises an exception:

        session = WebdriverSession(download_dir=Path("/data/downloads"))
        with session:
            session.driver.get("https://www.selenium.dev")
        # here the browser is already closed
    """

    def __init__(self, download_dir: Path):
        """
        Store the configuration of the session. The browser is NOT started here,
        only when the session is opened, so creating a session is cheap and
        has no side effects.
        """
        self.download_dir = download_dir
        self._driver: WebDriver | None = None

    @property
    def is_open(self) -> bool:
        """True while there is a browser running for this session."""
        return self._driver is not None

    @property
    def driver(self) -> WebDriver:
        """
        The running webdriver. Raises an exception instead of returning None
        when the session is closed, so a misuse fails with a clear message
        and not with "'NoneType' object has no attribute 'get'".
        """
        if self._driver is None:
            raise WebdriverSessionNotOpenException("webdriver session is not open")
        return self._driver

    def open(self) -> WebDriver:
        """
        Start the browser. A session holds a single browser, so opening it
        twice is an error: the first browser would be left running forever.
        """
        if self.is_open:
            raise WebdriverSessionAlreadyOpenException("webdriver session is already open")

        self._driver = get_chrome_webdriver(self.download_dir)
        return self._driver

    def close(self) -> None:
        """
        Quit the browser. It is safe to call more than once: closing a session
        that is already closed does nothing. The reference is cleared before
        quit(), so the session is marked as closed even if quit() fails.
        """
        driver, self._driver = self._driver, None
        if driver is not None:
            driver.quit()

    def __enter__(self) -> "WebdriverSession":
        """Called at the start of a `with` block: opens the session."""
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Called at the end of a `with` block, also when an exception was raised
        inside it: closes the session. It returns None, so the exception (if
        any) is not swallowed and keeps propagating.
        """
        self.close()
