# Система авторизации

Данный проект реализует систему авторизации с использованием Django и PostgreSQL. Функционал включает аутентификацию пользователей через номер телефона, верификацию номера, а также работу с реферальной системой.

## Основной функционал

Система позволяет пользователям аутентифицироваться через номера телефонов с использованием JWT токенов. Для подтверждения номера телефона реализован механизм одноразовых кодов (OTP). Также реализована реферальная система, где каждому пользователю выдается уникальный реферальный код, который позволяет приглашать других пользователей, сохраняя связь между пригласившим и приглашенным.

## Технологии

- Django и Django REST Framework для реализации API.
- PostgreSQL для работы с базой данных.
- Virtualenv для управления виртуальной средой.
- Heroku для деплоя приложения.

## Установка и запуск

Склонируйте репозиторий:
```
git clone https://github.com/sitoramonova/authorization
cd authorization
```
