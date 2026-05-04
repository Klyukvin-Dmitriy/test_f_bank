import os
import shutil
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("BASE_URL", "http://localhost:8000")


def _find_chrome_binary() -> str | None:
    for name in ("chrome", "google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        p = shutil.which(name)
        if p:
            return p

    # Common Windows locations (when not in PATH)
    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Google/Chrome/Application/chrome.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)

    return None


def _find_edge_binary() -> str | None:
    for name in ("msedge", "microsoft-edge", "microsoft-edge-stable"):
        p = shutil.which(name)
        if p:
            return p

    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)

    return None


@pytest.fixture()
def driver():
    preferred = os.environ.get("BROWSER", "chrome").lower()

    chrome_bin = _find_chrome_binary()
    edge_bin = _find_edge_binary()

    if preferred == "chrome" and chrome_bin:
        options = Options()
        options.binary_location = chrome_bin
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1400,900")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service, options=options)
    elif edge_bin:
        options = EdgeOptions()
        options.binary_location = edge_bin
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1400,900")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = EdgeService(EdgeChromiumDriverManager().install())
        drv = webdriver.Edge(service=service, options=options)
    else:
        raise RuntimeError("Не найден браузер Chrome/Edge для запуска Selenium. Установи Chrome или Edge.")

    drv.implicitly_wait(0)
    yield drv
    drv.quit()

