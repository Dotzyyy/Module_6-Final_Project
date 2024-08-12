# Module_6-Final_Project
## Final Project for UCD Fullstack Course
Precious Metals
Render Url: https://module-6-final-project.onrender.com
Github Url: https://github.com/Dotzyyy/Module_6-Final_Project
Super User: username: superadmin
            password: superpassword1234

## Concept

This project was created to simulate a marketplace where users could purchase precious metals, such as gold and silver. The prices are gathered using data from MetalpriceAPI

### Languages and Technology Used

Featured Languages:

* HTML5

* CSS3

* JavaScript

* Python3

* SQL

Featured Technologies:

* Postgresql

* pgadmin

* Bootstrap 

* Django

* AWS S3 (for image hosting)

* AWS SES (for password reset and newsletter subscription)

* Render (For deploying the app)

### Features



* Forms are available to help register, login, edit information and pruchase metal on the site.

* Forms for creating , updating and deleting news articles (Admin only).

* Requesting a new password be sent to your email (via AWS SES).

* Product pages where users can purchase metals by the gram

* A checkout system that allows users to purchase mutliples of various metals.

* Two tiered account system allowing users to purchase metals at a discounted price if they sign up as a 'wholesale' account.

* Pages to view all the products in a covenient location. (home page and all products page)








### Current Problems and Future Updates.

Some problems include unsatisfactory CSS which I chose not to obsess over too much as it can sometimes never feel complete and also get in the way of more pressing matters. In terms of features, I would have liked to apply a more in depth cart system that includes a way to add a users address and have a google maps view of location for the order confirmed screen. 
For the products page I would like to add more dimensions other than grams such as width, length and thickness.
I would also like to look into creating a graph that auto updates with the latest metal trends but I did not have time to investigate too far. Although perhaps pgadmins graph option could be utilised.



## How to run the database on render

### Step 1:

Sign in or create an account on https://render.com/

### Step 2:

On the Dashboard, create new PostgreSQL database and fill in the various details.

### Step 3:

Once created, download a database management software such as Postgresql and PgAdmin (optional).

### Step 4: 

Create a new server node, click properties and navigate to the connection tab.
Enter the following from the render database'S EXTERNAL URL:

* Host name/address. 

* Port should be automatic but look something like: 5432

* Maintenance database

* Username. For example: davidsexton

If entered correctly, the render database should appear in your servers.

### Step 5:

In your settings.py write something like 
"DATABASES = {
    'default': dj_database_url.parse(database_url)}
database_url = os.environ.get("DATABASE_URL")".

Later on in your render environment, make sure DATABASE_URL = the render databases INTERNAL_URL

### Step 6:

Use your terminal to type python manage.py migrate and then python manage.py makemigrations in order to create the database tables.

### Step 7:
At this point you'll need to have created the webservice so return to this step once that is complete.

Place an environment variable in the web service's environment tab called 'DATABASE_URL' and paste the Internal URL from the render database. 
Do not forget that the address should begin with 'postgresql'! / The rest of the environment variables will be provided on the UCD LMS

*Example: 'postgresql://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in' NOT ''postgres://davidsexton:hFNESpygwyQd4DMpWiBliSWZRbmwibRY@dpg-cpisitkf7o1s73bm97o0-a/flask_project_db_e6in'
            


## How to Deploy/Access the main website

### Step 1:

One of three options:

* Upload the project folder to your own github.

* Clone this git repository at: https://github.com/Dotzyyy/Module_6-Final_Project

* Access via the provided URL: https://module-6-final-project.onrender.com

### Step 2:
    
   Sign in or create an account on https://render.com/

### Step 3:

    Link your github account

### Step 4:

   Once logged in and on the main dashboard, select "New" > "Web Service".

### Step 5:

    Connect to this repository or a clone of it.

### Step 6:

On the following form, ensure that:

* You select an appropriate name for the web service

* Select your closest region (Frankfurt for Europe)

* Branch should be 'main'

* Run the following commands: pip install -r requirements.txt ; python manage.py migrate ; python manage.py collectstatic ; python manage.py ensure_adminuser
    Do not forget the ';' after each command

* Start Command 'gunicorn final_project.wsgi.application'

* Select Instance Type 'free

* Use the .env file provided in the zipfile on the UCD LMS / This will provide you with Database information, AWS information in order to access password reset and subscription services.

### Step 7:

Use the provided Url to access the website!:
    https://module-6-final-project.onrender.com

