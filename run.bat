call:run
exit


:run
python manage.py runserver
timeout 10
call:run