# My twitter backend for comment block
### Developed on a 64bit Ubuntu 18.04 System using vagrant and VirtualBox
1. In provision.sh: Install Django, MySQL, set up MySQL username and password, create a database 'twitter'.
2. In linux: run 'django-admin.py startproject twitter' then edit generated settings.py , i.e change allowed hosts and db settings.
3. In linux: run 'python manage.py migrate' to migrate then 'python manage.py createsuperuser'.(admin)
4. Install Django rest framework, edit settings.py, and follow 'https://www.django-rest-framework.org/tutorial/quickstart/', just to make the server start working
5. ...