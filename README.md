GEOSHIPS APP
***

MODELS:
    <li> Vessel
    <li> History

API:
    <li> list vessels ---> api/vessels/
    <li> History by ship ---> id api/history/id

API реализован как для владельцев так и для админа.

Владелец может просматривать свои данные по судну и историю передвежений своих суден.
Запросы делаются с помощью токена, который будет выдавать админ приложения.
В Headers передаем следующее {'Authorization': 'token tokenFHJSG312632', 'Content-Type': 'application/json'} при запросе данных.
Данные получить нельзя без помощи токена.
Если запрос делает админ, он получает все что есть по запросам.

Так же в админке можно как назначить владельца, так и убрать.


Выгрузка данных из .xlsx файлов в нашу базу данных.
Реализована периодичная функция с помощью celery periodic task crontab.
Функция запускается каждую полночь т.е 00:00.
Функция просматривает все файлы, которые мы имеем в нашей директории(указана в settings, при желании можно руками изменить пути), затем, как мы загрузили все данные,
файлы перемещаются в другую папку, для будущего хранения на всякий случай.


***

Инструкция по развертыванию приложения


1. sudo apt-get update && sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

2. git clone https://github.com/Khanze99/geoship_app.git

3. Создание виртуального окружения virtualenv venv

4. pip3 install -r requirements.txt

5. Создание базы данных
    sudo -u postgres psql

    CREATE DATABASE database_db;
    CREATE USER admin with password 'password';
    GRANT ALL PRVILEGES ON DATABASE database_db to admin;

    \q

6. export POSTGRES_GEOSHIP_DB=database_db
    export POSTGRES_GEOSHIP_PASSWORD=ConeForest1928

7. Меняем в nginx/geo_uwsgi.ini настройки под свою систему

8. sudo ln -s nginx/geo_nginx.cong /etc/nginx/sites-enabled/

9. sudo service nginx restart

10. Создаем нашего админа python3 manage.py createsuperuser

10. Подгружаем модели и устанавливаем статику cd geoship_app && python3 manage.py migrate && python3 manage.py collectstatic

10. Запускаем в terminal1 uwsgi -ini nginx/geo_uwsgi.ini

11. Запускаем celery в terminal2 cd geoship_app/ && celery -A geoship_app worker -l info -B  -- Запуск периодического таска на заливание данных в бд

