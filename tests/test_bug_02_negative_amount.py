from tests.pages.transfer_page import TransferPage


def test_negative_amount_should_be_rejected(driver, base_url):
    """
    Ожидаем корректное поведение: отрицательная сумма должна быть запрещена.
    Текущая реализация позволяет отрицательные суммы → тест должен падать (красный CI).
    Дефект: https://github.com/Klyukvin-Dmitriy/test_f_bank/issues/2
    """
    page = TransferPage(driver, base_url).open("/")
    page.select_rub_account()
    page.enter_card_number("1111111111111111")
    page.enter_amount("-20000")

    assert not page.is_transfer_button_present(), "Кнопка «Перевести» не должна быть доступна при отрицательной сумме"

