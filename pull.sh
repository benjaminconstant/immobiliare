source `which virtualenvwrapper.sh`
workon invernizzi-CMS
git pull
cd django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo yes | python manage.py collectstatic