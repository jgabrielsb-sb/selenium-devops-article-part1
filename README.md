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

The script opens Chrome, downloads a file from the Selenium website, closes Chrome and prints where the file was saved:

```
Downloaded /path/to/this/repo/downloads/file_1.txt (14 bytes)
```

The two Selenium Manager examples from section 2 are standalone scripts:

```bash
uv run src/with_selenium_manager.py      # pins Chrome 155 with browser_version
uv run src/without_selenium_manager.py   # needs a chromedriver you downloaded to drivers/chromedriver
```

## Changing the download folder

By default, files go to `downloads/` at the project root. Set the `DOWNLOAD_DIR` environment variable to change it (for example on a server or in a container):

```bash
DOWNLOAD_DIR=/data/downloads uv run src/main.py
```

The folder is checked before the browser opens. The path must be absolute and writable, otherwise the script stops with a clear error:

```bash
$ DOWNLOAD_DIR=media uv run src/main.py
ValueError: download_dir must be an absolute path, got 'media'

$ DOWNLOAD_DIR=/media uv run src/main.py
PermissionError: download_dir '/media' is not writable
```

## Steps

| Tag | What it shows | Article section |
|---|---|---|
| `part-1/01-broken` | First version: `DOWNLOAD_DIR = Path("media")` hard-coded in `main.py`, and `run()` quits the browser right after the click. No error, and the download never arrives. | 3. Serving the Webdriver |
| `part-1/02-settings` | `settings.py` with `DOWNLOAD_DIR`, `set_download_default_dir` validating the folder, and the automation waiting for the download | 3.2. Centralized settings and a validated download directory |
| `part-1/03-session` | `WebdriverSession` owns the browser's lifecycle; the base class's `run()` opens and closes it, and each automation only implements `_run()` (final code) | 3.3. Managing Webdriver Sessions Effectively |

Check out a step with:

```bash
git checkout part-1/01-broken
git checkout part-1/02-settings
git checkout part-1/03-session
```

Go back to the latest code with `git checkout main`.

## Coming next

- **Selenium Hub in Docker:** our automations connect to browsers running in containers, managed by a Selenium Hub.
- **Dockerizing the application:** Python, Selenium and our settings run inside a container too.
- **Webdriver factories:** configured webdrivers (headless, proxy, Firefox, ...) for each automation.
