<!-- УРЛ-шотер на основе Django -->

Мой учебный проект, который я разработал при получении тестового задания от компании.
Задание было написать сокрашатель ссылок не используя другие API.
Реализация очень простая без настроек указания длины(фиксировано 6 символов), при этом символы будут случайны в новой укороченной ссылке.
Если другой пользователь захочет укоротить ссылку, которая уже есть в БД, он получит результат из БД.

Для того, чтобы скопировать себе полностью рабочий вариант, нужно клонировать ветку deploy.
Это даст Вам почти предпусковую версию для размешения на VPS.
По сути для полного запуска нужно клонировать ветку deploy и после на самом сервере внести изменения в конфиги nginx, чтобы заработало доменное имя и SSL.

Буду рад замечаниям. Спасибо.

<!-- Стек -->
Python
Poetry(вместо pip)
Django
PostgreSQL
Gunicorn
Nginx
Docker | Docker-compose
Git

<!-- Лицензия -->

MIT
