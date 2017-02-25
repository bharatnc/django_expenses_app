##Django expenses application for mangaging your expenses.

##Requirements/Dependencies

1. Python pip
2. Django version of 1.9 installed
3. Django crispy_forms
4. Django Queryset CSV v1.0.0 
5. Python xlwt 1.2.0

##Installing Requirements/Dependencies
1. Python pip - Install Python pip using `sudo apt-get install python-pip`.
2. Django v 1.9 - Install using `sudo pip install django==1.9`.
3. Django crispy form - Install using `sudo pip install --upgrade django-crispy-forms`.
4. Django Queryset CSV v 1.0.0 - Install using `sudo pip install django-queryset-csv`.
5. Python xlwt 1.2.0 - Install using `sudo pip install xlwt`

##Features
**Yes** Add expenses <br>
**Yes** Edit/modify expenses <br>
**Yes** Export Expenses in .XLS format <br>
**Yes** Export expenses in .CSV format <br>
**Yes** Restore deleted expenses from trash <br>
**Yes** Delete expenses permenantly <br>
**Yes** Delete expenses permenantly <br>
Display expenses by month <br>
Search for an expense<br>
Restore Individual items from trash <br>
Export custom elements <br>


##Setup
1. After installing the requirements, run `sudo python manage.py migrate` and `sudo python manage.py makemigrations`.
2. Next, run the Django webserver using `sudo python manage.py runserver ip_address:port_no`.
3. **[OPTIONAL]** To create and set up a admin account use `python manage.py createsuperuser`. Enter the username, email-address and password to set it up.


## Customize the UI!

1. Well this expenses app does not have a very attractive UI, but does the job quite well.
2. All of the templates use bootstrap CDN for CSS and JQuery.
3. Alter the templates in `templates` directory - as per your need.
4. Add a static folder - if you do not want to use CDN. In the `settings.py` file under the `expenses_project` folder, add this `STATIC_URL = '/static/'`.
5. For details on referencing your local llibraries and images, read [this](https://docs.djangoproject.com/en/1.10/intro/tutorial06).

##General directory Structure:


expenses_app (main folder)<br>
	---- expenses (app) <br>
	---- expenses_project (project) <br>
	---- main (app) <br>
	---- templates <br>
	---- manage.py <br>

The `main (app)` acts as a platform for the `expenses(app)`. You can add more apps like expenses. Use the main as a landing page for accessing these apps.

