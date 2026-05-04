from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class TransferPageLocators:
    # Account cards
    RUB_ACCOUNT = (By.XPATH, "//*[self::h2][normalize-space()='Рубли']")
    USD_ACCOUNT = (By.XPATH, "//*[self::h2][normalize-space()='Доллары']")

    # Inputs (appear after selecting account; amount appears after 16+ digits card)
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='0000 0000 0000 0000']")
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='1000']")

    # Status / actions
    INSUFFICIENT_FUNDS = (By.XPATH, "//*[contains(normalize-space(),'Недостаточно средств')]")
    TRANSFER_BUTTON = (By.XPATH, "//button[normalize-space()='Перевести']")

