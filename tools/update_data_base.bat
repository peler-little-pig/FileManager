echo Data will gone!

del db.sqlite3

python manage.py makemigrations

python manage.py migrate