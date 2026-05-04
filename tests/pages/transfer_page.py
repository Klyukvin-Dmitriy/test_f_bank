from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import TransferPageLocators as L


class TransferPage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "/") -> "TransferPage":
        self.driver.get(f"{self.base_url}{path}")
        return self

    def select_rub_account(self) -> "TransferPage":
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.RUB_ACCOUNT)).click()
        return self

    def select_usd_account(self) -> "TransferPage":
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(L.USD_ACCOUNT)).click()
        return self

    def enter_card_number(self, digits16: str) -> "TransferPage":
        card = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(L.CARD_NUMBER_INPUT))
        card.clear()
        card.send_keys(digits16)
        return self

    def enter_amount(self, amount_str: str) -> "TransferPage":
        amount = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(L.AMOUNT_INPUT))
        amount.clear()
        amount.send_keys(amount_str)
        return self

    def is_transfer_button_present(self) -> bool:
        return len(self.driver.find_elements(*L.TRANSFER_BUTTON)) > 0

    def is_insufficient_funds_visible(self) -> bool:
        return len(self.driver.find_elements(*L.INSUFFICIENT_FUNDS)) > 0

