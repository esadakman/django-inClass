-- virtualenv nameofyourvitualenv
-- cd nameofyourvitualenv

(For Windows Users) Go to Scripts directory inside your virtualenv and activate virtualenv

- cd Scripts
- activate

---

-.\envname\Scripts\activate
-pip freeze (kontrol için)

---

Install Django

- pip install django

Return to your virtualenv directory

- cd ..

Start a project by following command

-- django-admin startproject nameofyourproject
-- django-admin startproject nameofyourproject .

Change directory to your project

- cd nameofyourproject

Start the server by following command

- python manage.py runserver

APP
-- python manage.py startapp firstApp

Requirementsları kaydetmek için
pip freeze > requirements.txt

powerShell
set-executionpolicy remotesigned
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
