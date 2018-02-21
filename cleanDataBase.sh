rm -rf quiz/migrations
rm db.sqlite3
./manage.py makemigrations quiz
./manage.py migrate
./manage.py migrate quiz
