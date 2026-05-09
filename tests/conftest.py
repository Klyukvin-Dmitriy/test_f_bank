import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("BASE_URL", "http://localhost:8000")


@pytest.fixture()
def driver():
    """
    Selenium 4 содержит Selenium Manager: драйвер подбирается автоматически под установленный браузер.
    Это устраняет типичную проблему несовпадения версий Chrome ↔ ChromeDriver в CI.
    """
    preferred = os.environ.get("BROWSER", "chrome").lower()

    if preferred == "edge":
        options = EdgeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1400,900")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Edge(options=options)
    else:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1400,900")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(options=options)

    drv.implicitly_wait(0)
    yield drv
    drv.quit()

