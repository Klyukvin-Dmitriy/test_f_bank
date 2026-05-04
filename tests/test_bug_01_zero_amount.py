from tests.pages.transfer_page import TransferPage


def test_zero_amount_should_be_rejected(driver, base_url):
    """
    Ожидаем корректное поведение: сумма 0 должна быть запрещена.
    Текущая реализация позволяет перевод 0 → тест должен падать (красный CI).
    """
    page = TransferPage(driver, base_url).open("/")
    page.select_rub_account()
    page.enter_card_number("1111111111111111")
    page.enter_amount("0")

    assert not page.is_transfer_button_present(), "Кнопка «Перевести» не должна быть доступна при сумме 0"

