Here was creating a Notes Saving Application 
We are using FLASK module/framework - which is lightweight than django

installing flask and other modules
========
pip install flask

pip install flask-login

pip install flask-sqlalchemy

- in __init__.py we set up the flask application 

- in auth.py and views.py we define the routes of the respective pages and that path mentioned give sthe respective pages 
    Eg:
    auth.py
    =========
    #Defining login , Logout & sign up 

    from flask import Blueprint

    auth = Blueprint('auth',__name__) 

    @auth.route('/login')
    def login():
        return "<p>login</p>"

    @auth.route('/logout')
    def logout():
        return "<p>logout</p>"

    @auth.route('/sign-up')
    def sign_up():
        return "<p>Sign Up</p>"

-  In template we create html files for respective login pages using jinja- jinja is a templating language 
   Templating language helps to write some python inside of html documents - no need to know javascript - display user information without javascript 

-  Inside Template folder create base.html

- POST request - means we are making some changes to the db or website - post with all the info in the form 

- GET request - retrieving information 

- 

