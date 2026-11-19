# It Works on My Machine — Part 1

Companion code for the first article in the series "It Works on My Machine", about running Selenium automations in Python the same way everywhere: [Part 1 on Medium](<MEDIUM_LINK>).

The repository is built step by step. Each tag is the code at one point in the article (see [Steps](#steps)).

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.10+ (uv can install it for you)
- Google Chrome. If it is not installed, or when a version is pinned with `browser_version`, Selenium Manager downloads Chrome for Testing.

## How to run

```bash
uv sync
uv run src/main.py
```

At this step, the script opens Chrome, clicks the download link and closes Chrome. No error is shown, but the download never ends up in `media/`. Section 3.1 of the article explains why.

The two Selenium Manager examples from section 2 are standalone scripts:

```bash
uv run src/with_selenium_manager.py      # pins Chrome 155 with browser_version
uv run src/without_selenium_manager.py   # needs a chromedriver you downloaded to drivers/chromedriver
```

## Steps

| Tag | What it shows | Article section |
|---|---|---|
| `part-1/01-broken` | First version: `DOWNLOAD_DIR = Path("media")` hard-coded in `main.py`, and `run()` quits the browser right after the click | 3. Serving the Webdriver |

Check out a step with:

```bash
git checkout part-1/01-broken
```

Go back to the latest code with `git checkout main`.

## Coming next

- **Selenium Hub in Docker:** our automations connect to browsers running in containers, managed by a Selenium Hub.
- **Dockerizing the application:** Python, Selenium and our settings run inside a container too.
- **Webdriver factories:** configured webdrivers (headless, proxy, Firefox, ...) for each automation.
