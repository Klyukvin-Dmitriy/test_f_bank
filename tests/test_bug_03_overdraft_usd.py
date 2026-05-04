from tests.pages.transfer_page import TransferPage


def test_usd_overdraft_should_be_rejected(driver, base_url):
    """
    Ожидаем корректное поведение: при выборе USD счёта (баланс 100 $) нельзя перевести 1000 $.
    В приложении логика недостатка средств зависит от query params balance/reserved, а не от баланса выбранного счёта.
    Мы специально открываем страницу с большим RUB balance, чтобы дефект проявился и тест упал (красный CI).
    """
    page = TransferPage(driver, base_url).open("/?balance=100000&reserved=0")
    page.select_usd_account()
    page.enter_card_number("1111111111111111")
    page.enter_amount("1000")

    assert page.is_insufficient_funds_visible(), "Должно отображаться «Недостаточно средств…» для USD перевода сверх баланса"
    assert not page.is_transfer_button_present(), "Кнопка «Перевести» не должна быть доступна при USD переводе сверх баланса"

