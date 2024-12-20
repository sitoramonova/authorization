# Система авторизации

Данный проект реализует систему авторизации с использованием Django и PostgreSQL. Функционал включает аутентификацию пользователей через номер телефона, верификацию номера, а также работу с реферальной системой.

## Основной функционал

Система позволяет пользователям аутентифицироваться через номера телефонов с использованием JWT токенов. Для подтверждения номера телефона реализован механизм одноразовых кодов (OTP). Также реализована реферальная система, где каждому пользователю выдается уникальный реферальный код, который позволяет приглашать других пользователей, сохраняя связь между пригласившим и приглашенным.

## Технологии

- Django и Django REST Framework для реализации API.
- PostgreSQL для работы с базой данных.
- Virtualenv для управления виртуальной средой.


## Установка и запуск

Склонируйте репозиторий:
```
git clone https://github.com/sitoramonova/authorization
cd authorization
```
Создайте виртуальное окружение и активируйте его:

```
python3 -m venv .venv
source .venv/bin/activate
```

Установите зависимости:

```
pip install -r requirements.tx
```
Примените миграции базы данных:

```
python manage.py migrate
```
Запустите локальный сервер разработки:

```
python manage.py runserver
```

## Postman

Файл Referral System API.postman_collection.json содержит коллекцию запросов для тестирования API системы авторизации и реферальной системы с помощью Postman.

##
