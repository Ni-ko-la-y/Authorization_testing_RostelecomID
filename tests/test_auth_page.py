import time
import pytest
from pages.auth_page import AuthPage
from config import name, surname, valid_email2, valid_password2, negative_email, negative_telephone
from config import telephone, negative_pass, valid_email, pass_telecom, captcha

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py


def test_1(web_browser):
    """Позитивный тест перехода на страницу подтверждения почты при регистрации"""

    page = AuthPage(web_browser)

    """Переход на страницу регистрации, заполнение полей ввода
    корректными данными, клик на Зарегистрироваться"""
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()

    """Проверяем отправку кода подтверждения email"""
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_2_negative(web_browser):
    """Негативный тест получения кода подтверждения email при отправке некорректного адреса почты."""

    page = AuthPage(web_browser)

    """Переход на страницу регистрации, ввод несуществующего email,
    остальные данные корректны, клик на Зарегистрироваться"""
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(negative_email)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()

    """Проверяем отправку кода подтверждения email"""
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_3_negative(web_browser):
    """Негативный тест получения кода подтверждения телефона при отправке некорректного номера."""

    page = AuthPage(web_browser)

    """Переход на страницу регистрации, ввод некорректного номера телефона,
    остальные данные корректны, клик на Зарегистрироваться"""
    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(negative_telephone)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()

    """Проверяем отправку кода подтверждения телефона"""
    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()


def test_4_negative(web_browser):
    """Негативный тест авторизации в системе через телефон"""

    page = AuthPage(web_browser)

    """Вводим некорректные данные"""
    page.field_mail.send_keys(telephone)
    page.field_pass.send_keys(negative_pass)
    page.button_come_in.click()

    """Проверяем наличие сообщения об ошибке"""
    assert "Неверный логин или пароль" in page.log_pass_error.get_text()


def test_5(web_browser):
    """Авторизация в системе через email"""

    page = AuthPage(web_browser)
    web_browser.implicitly_wait(5)

    """Вводим некорректные данные"""
    page.field_mail.send_keys(valid_email)
    page.field_pass.send_keys(pass_telecom)
    page.button_come_in.click()

    """Проверка входа в личный кабинет"""
    if page.avatar_user.is_presented():
        assert True
    else:
        assert False


def test_6_negative(web_browser):
    """Негативный тест авторизации в системе через почту"""

    page = AuthPage(web_browser)

    """Вводим некорректные данные"""
    page.field_mail.send_keys(valid_email)
    page.field_pass.send_keys(negative_pass)
    page.button_come_in.click()

    """Проверяем наличие сообщения об ошибке"""
    assert "Неверный логин или пароль" in page.log_pass_error.get_text()


def test_7_negative(web_browser):
    """Негативный тест восстановления пароля"""

    page = AuthPage(web_browser)

    """Клик по ссылке Забыл пароль, заполнение полей ввода некорректными данными"""
    page.link_forgot_pass.click()
    page.field_phone.send_keys(negative_telephone)
    page.field_captcha.send_keys(captcha)
    page.button_proceed.click()

    """Проверяем наличие сообщения об ошибке"""
    assert "Неверный логин или текст с картинки" in page.log_text_error.get_text()


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_8(web_browser):
    """Проверка присутствия ссылки на политику конфиденциальности"""

    page = AuthPage(web_browser)

    """Клик по ссылке Зарегистрироваться"""
    page.link_register.click()

    """Проверка присутствия ссылки"""
    assert "политику конфиденциальности" not in page.treaty.get_text()


@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_9(web_browser):
    """Проверка присутствия продуктового слогана на странице регистрации"""

    page = AuthPage(web_browser)

    """Клик по ссылке Зарегистрироваться"""
    page.link_register.click()

    """Проверяем присутствие слогана"""
    assert "Персональный помощник в цифровом мире Ростелекома" not in page.left_block.get_text()


# def test_10(web_browser):
#     """Получить информацию о привязке соц. сети к личному кабинету. """
#
#     page = AuthPage(web_browser)
#
#     """Клик по кнопке соц. сети VK"""
#     page.button_VK.click()
#
#     """Проверяем наличие вспомогательной информации."""
#     if page.bind_soc_network.is_presented():
#         assert True
#     else:
#         assert False
#
#
# def test_11(web_browser):
#     """Авторизация в ЛК с помощью соц. сети Одноклассники"""
#
#     page = AuthPage(web_browser)
#
#     """Клик по кнопке Одноклассники"""
#     page.button_OK.click()
#
#     """Проверяем вход в ЛК"""
#     if page.avatar_user.is_presented():
#         assert True
#     else:
#         assert False


def test_12(web_browser):
    """Переход на страницу Яндекс.паспорт"""

    page = AuthPage(web_browser)

    """Клик по кнопке Яндекс"""
    page.button_yandex.click()

    """Проверяем переход в Яндекс.паспорт"""
    if page.logo_yandex.is_presented():
        assert True
    else:
        assert False
