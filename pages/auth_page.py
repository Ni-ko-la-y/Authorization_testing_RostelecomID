import os

from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = os.getenv("LOGIN_URL") or 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    # email = WebElement(id='email')
    # password = WebElement(id='pass')
    # btn = WebElement(class_name='btn.btn-success')

    """-------------------------Страница авторизации------------------------"""
    """Ссылка Зарегистрироваться"""
    link_register = WebElement(css_selector='#kc-register')

    """Ссылка Забыл пароль"""
    link_forgot_pass = WebElement(id="forgot_password")

    """Поля ввода email и пароль"""
    field_mail = WebElement(id="username")
    field_pass = WebElement(id="password")

    """Кнопка Войти"""
    button_come_in = WebElement(id="kc-login")

    """Слоган компании"""
    tagline = WebElement()

    """Сообщение об ошибке - Неверный логин или пароль"""
    log_pass_error = WebElement(xpath='//*[@id="page-right"]//p')

    """Аватар пользователя в личном кабинете"""
    avatar_user = WebElement(xpath='//*[@class="user-info__name-container"]//img')

    """-------------------------Страница регистрации-------------------------"""
    """Кнопка Зарегистрироваться"""
    button_reg = WebElement(name="register")

    """Поля ввода имени и фамилии"""
    field_name = WebElement(name='firstName')
    field_surname = WebElement(name='lastName')

    """Поля ввода email, пароля, подтверждения пароля"""
    field_reg_email = WebElement(id='address')
    field_reg_pass = WebElement(name="password")
    field_confirm = WebElement(name="password-confirm")

    """Элемент подтверждения отправки кода """
    confirmation = WebElement(xpath='//div[@class="card-container__content"]/p')

    """Левый блок формы регистрации"""
    left_block = WebElement(id="page-left")

    """Информация принимаемых условий в договорах"""
    treaty = WebElement(xpath='//div[@class="auth-policy"]')

    """-------------------------Страница восстановления пароля----------------"""
    """Поля ввода телефона и капчи"""
    field_phone = WebElement(id='username')
    field_captcha = WebElement(id='captcha')

    """Кнопка Продолжить"""
    button_proceed = WebElement(id='reset')

    """Сообщение об ошибке - Неверный логин или текст с картинки"""
    log_text_error = WebElement(xpath='//*[@id="page-right"]//p[1]')

    """------------------------Социальные сети-----------------------"""

    """Кнопки социальных сетей"""
    button_VK = WebElement(id="oidc_vk")
    button_yandex = WebElement(id="oidc_ya")
    button_OK = WebElement(id="oidc_ok")

    """Логотип Яндекс в Яндекс.паспорт"""
    logo_yandex = WebElement(xpath='//div[@class="Header-yaLogoBlock"]/a')

    # """Информация о привязке социальной сети к личному кабинету"""
    # bind_soc_network = WebElement(xpath='//p[contains(text(), "в настройках привяжите социальные сети")]')


