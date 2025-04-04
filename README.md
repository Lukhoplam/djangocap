# Django Capstone Project

This is a Django-based capstone project. The repository contains the necessary files to run a Django application, along with configuration files for different environments.

To install and run this project on your local machine, follow the instructions below.

1. **Clone the Repository**:
   git clone [repo]
   cd djangocapstone
2. **You need to install the dependencies listed in the requirements.txt file**:
  pip install -r requirements.txt
3. **Create a Virtual Environment: On Windows**
   python -m venv .venv
4. **Activate**
  .\.venv\Scripts\activate
5. **Migrate the Database: Run the migrations to create the necessary tables in the database**
   python manage.py migrate
6.**Create a Superuser: Create a superuser to access the Django admin**
   python manage.py createsuperuser
7. **Start the Development Server**
   python manage.py runserver
then :Open your browser and visit http://127.0.0.1:8000/ to access the app.
To access the Django admin, go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created.
