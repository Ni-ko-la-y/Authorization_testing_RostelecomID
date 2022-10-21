# Authorization_testing_RostelecomID
Тестирование нового интерфейса авторизации в личном кабинете от заказчика "Ростелеком Информационные технологии."


1) Install all requirements:
   pip3 install -r requirements.txt

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads
   (choose version which is compatible with your browser)

3) Run tests:
   python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*


WebDriver должен быть расположен в корневой папке каталога.

Команды для запуска файлов с тестами:

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_by_code.py