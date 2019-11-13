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
Данные получить нельзя без помощи токена.
Если запрос делает админ, он получает все что есть по запросам.

Так же в админке можно как назначить владельца, так и убрать.


Выгрузка данных из .xlsx файлов в нашу базу данных.
Реализована периодичная функция с помощью celery periodic task crontab.
Функция запускается каждую полночь т.е 00:00.
Функция просматривает все файлы, которые мы имеем в нашей директории(указана в settings), затем, как мы загрузили все данные,
файлы перемещаются в другую папку, для будущего хранения на всякий случай.

uwsgi --socket geoship.sock --wsgi-file geoship_app/wsgi.py --chmod-socket=666