# Job Application Website
A python-based DJANGO application that submit user input and cv file following provided APIs and restrictions to designated server.

## Interface
* Login Page to authenticate.
* Details Submission page to sumbit the cv file and other information specified in the docs.
* Success page to indicate successfull submission.

## How to build on your pc
1. `git clone https://github.com/nion068/application_assignment.git`
2. `cd application_assignment`
3. `pip install venv` to create your environment
4. `source venv/bin/activate` to enter the virtual  environment
5. `pip install -r requirements.txt` to install the requirements in the current environment
6. Run `python manage.py migrate`
7. Then `python manage.py makemigrations apply`
8. Again run `python manage.py migrate`
9. `python manage.py runserver` to start the development server.
10. Open http://127.0.0.1:8000/apply/ to enter login credentials.
