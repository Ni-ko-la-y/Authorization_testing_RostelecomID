import time
import pytest
from pages.auth_by_code import Auth_By_Code
from config import valid_email, negative_email, negative_telephone


# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_by_code.py


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_13_negative(web_browser):
    """Проверка отправки кода подтверждения на несуществующий адрес почты"""

    page = Auth_By_Code(web_browser)

    """Ввод некорректного email и клик по кнопке Получить код"""
    page.field_email_phone.send_keys(negative_email)
    page.button_get_code.click()

    """Проверка отправки кода подтверждения"""
    assert "Код подтверждения отправлен" in page.send_confirm.get_text()

    """Ожидание в 120 секунд необходимо для обхода системы безопасности. 
    Если убрать ожидание, проходить будет только первый тест в очереди, 
    остальные будут падать"""
    time.sleep(120)


def test_14(web_browser):
    """Переход на страницу отправки кода подтверждения"""

    page = Auth_By_Code(web_browser)

    """Ввод корректного email и клик по кнопке Получить код"""
    page.field_email_phone.send_keys(valid_email)
    page.button_get_code.click()

    """Проверка отправки кода подтверждения"""
    assert "Код подтверждения отправлен" in page.send_confirm.get_text()
    time.sleep(120)


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_15_negative(web_browser):
    """Проверка отправки кода подтверждения на некорректный номер телефона"""

    page = Auth_By_Code(web_browser)

    """Ввод некорректного номера и клик по кнопке Получить код"""
    page.field_email_phone.send_keys(negative_telephone)
    page.button_get_code.click()

    """Проверка отправки кода подтверждения"""
    assert "Код подтверждения отправлен" in page.send_confirm.get_text()

