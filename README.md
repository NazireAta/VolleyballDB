After cloning the repository to your local environment, the necessary libraries should be installed by running "pip install -r requirements.txt".

You should update your mysql username and password in "volleyball\settings.py".

After that, run "python manage.py migrate" and "python manage.py runserver". The site will be avaliable at "http://127.0.0.1:8000/".

You will be directed to the login page. After you login to the system, you will be redirected to related user page.

You can see other types of users' pages but the information and buttons won't be functional if your role doesn't match.

You can perform the operations tha your role allowes you to.

To go back to login page just go back to "http://127.0.0.1:8000/" or "http://127.0.0.1:8000/login". That way you can login as another user.
