# Deployment

To ensure a smooth submission process, I made an initial effort to deploy this project on Heroku as early as possible. 
This allowed me to work through any potential issues and make necessary adjustments with ample time before the submission deadline.

Below are the detailed steps that were carefully followed the **Code Institute** guides to ensure that everything worked seamlessly and without any issues.


## Deploying on Heroku

In order to deploy a basic application on Heroku using Github, the following steps were taken:

1. Install Django with required packages
2. Create a new Django project
3. Deploy project to Heroku
4. Set up project to use a relational database (PostgreSQL)
5. Connect Heroku to the PostgreSQL database

## Install Django with required packages.

*Django*, a full stack framework will support this project.

To install, type *pip3 install 'Django'* into the terminal.

![Django installation](static/readme/deployment/install-django.png)

Install gunicorn (web server) by typing *pip3 install gunicorn*.

![Gunicorn installation](static/readme/deployment/install-gunicorn.png)

Install the dj_database_url library for postgreSQL by typing *pip3 install dj_database_url*, then install the psycopg2 library for postgreSQL by typing *pip3 install psycopg2-binary*.

![Dj-database-url installation](static/readme/deployment/install-dj-database-url.png)

![Psycopg2-binary installation](static/readme/deployment/install-psycopg2-binary.png)

Create a requirements.txt file in the main directory. 

In the terminal, type *pip3 freeze --local > requirements.txt*.  This file tells Heroku what packages are needed to run the deployed application.  Follow this step each time a new package is installed.

![Freeze --local](static/readme/deployment/freeze.png)

![Requirements](static/readme/deployment/requirements.png)

## Create a new Django project.

I created a new *project* called *it_project* typing the following to the terminal, `django-admin startproject it_project`
This will create new folder called `it_project` and a `manage.py` file in the root directory.

![Start Project](static/readme/deployment/startproject.png)

![Start Project](static/readme/deployment/admin-startproject.png)

Next step, I created an app called `restaurant` within the project. Type *python3 manage.py startapp restaurant*. This app will act as the homepage.

![Start App](static/readme/deployment/startapp.png)

![Start App](static/readme/deployment/app.png)

After I opend the `settings.py` file in the `it_project` **project** folder and add the newly created *restaurant* app to the bottom of the Installed Apps list. (Add a comma to the end even though it's the last list entry.)

![Stalled Apps Settings](static/readme/deployment/installed-apps1.jpg)

 - In views.py, import HttpResponse from django.http at the top of the file, *from django.http import HttpResponse*
 - Add the following view function to return a HttpResponse of "Hello, World!" *def my_restaurant(request): return HttpResponse("Hello, World!")*
 - In *it_restaurant/urls.py* import the *my_restaurant view*: *from restaurant.views import my_resaturant*.
 - Add the new path to the urlpatterns: *path('restaurant/', my_resaturant, name='restaurant')*,

In the terminal, type *python3 manage.py migrate* to update the database schema used by Django.  

![Migrate](static/readme/deployment/migrate.png)

In the terminal, type *python3 manage.py runserver* to verify local deployment. Append */restaurant* to the end of the URL in the browser. An error message open in the browser. Copie the hostname between the square brackets in the error message to ALLOWED_HOSTS in the *it_project/settings.py* file, and add *,'.herokuapp.com'* and saved it.

![Allowed Hosts ](static/readme/deployment/allowed_hosts.png)

Confirm the text *Hello, World!* is displayed on the page.

## Deploy project to Heroku

Create the Heroku app:

1. Navigate to your Heroku dashboard and create a new app with a unique name in a region close to you.
2. In your new app's settings tab, ensure the Config Var DISABLE_COLLECTSTATIC key has a value of 1.
3. A Procfile is needed in the main directory to tell Heroku the commands that are to be executed by the app on startup. In this case we need to start a web server (gunicorn).

![Procfile ](static/readme/deployment/procfile.png)

4. Click on the Deploy tab in your Heroku app dashboard, connect to your GitHub repo and click on Deploy Branch.
5. Click the Open app button to see your deployed app.



## Set up project to use a relational database (PostgreSQL)

For this project, an account was created for **ElephantSQL** that is a PostgreSQL database hosting service that uses several cloud-hosted platforms. 

The steps to create a PostgreSQL instance were followed according to the Code Institute course and can be done by following the steps below:


### Create PostgreSQL instance

Log into ElephantSQL to access your dashboard:

1. Click Create New Instance:

![ElephantSQL ](static/readme/deployment/elephant1.png)

2. Set up your plan:

 - Give your plan a Name (this is commonly the name of the project).
 - Select the Tiny Turtle (Free) plan.
 - You can leave the Tags field blank.
 - Then click Select Region.

![ElephantSQL ](static/readme/deployment/elephant2.png)

3. Select a data centre near you
4. Click Review.
5. Check your details are correct and then click Create instance.
6. Click on your newly named instance.

![ElephantSQL ](static/readme/deployment/elephant3.png)

7. If your PostgreSQL version is 12 or higher then click on DETAILS and copy the URL.

![ElephantSQL ](static/readme/deployment/elephant4.png)

### Connect database to code

8. Return to your workspace and open the *it_project/settings.py* file. Change the value of *DEBUG* to *True*
9. Create a file named env.py at the top level of the project.
10. Open the .gitignore file and add env.py to prevent the secret data you will add to it from being pushed to GitHub.
11. In your newly created env.py file, import Python's operating system module and use it to set the value of the DATABASE_URL constant to the URL you copied from ElephantSQL.

![ElephantSQL ](static/readme/deployment/elephant5.png)

12.  In it_project/settings.py, import the appropriate packages.

![ElephantSQL ](static/readme/deployment/elephant6.png)

13. Next in the settings.py file, you need to comment out the local sqlite3 database connection and then connect to the environment variable DATABASE_URL you previously added to the env.py file.

![ElephantSQL ](static/readme/deployment/elephant7.png)

14. Now that the project is connected to the database, you can create database tables with Django's migrate command *python3 manage.py migrate*.

15. Deploy the project. Return to your workspace and open the it_restaurant/settings.py file. Change the value of DEBUG back to False as this will ensure the production deployed app is secure. Git add, commit and push your updated code to GitHub. Return to your Heroku dashboard and go to your it_restaurant app. Click on the Deploy tab. Do a manual deployment.


## Connect Heroku to the PostgreSQL database

1. Once the deployment is complete click on Reveal Config Vars in the Settings tab on Heroku.
2. Add a new config var with a key of DATABASE_URL and the value of the ElephantSQL URL.

![Config. Vars ](static/readme/deployment/config-vars.png)

Now your deployed app is connected to your PostgreSQL cloud database.

**These steps are current to the time of deployment and may change in the future.**

Back to Readme file [README.md](README.md)
