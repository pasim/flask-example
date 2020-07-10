Flask coding example

What this example does

- Creates a new Python-based application utilising Flask Framework
- Renders the list of stores from the app/data/stores.json file in alphabetical order using a template.
- Using postcodes.io to get the latitude and longitude for each postcode. Renders them underneath each store location in the template.
- Provides the functionality that allows to return a list of stores in a given radius of a given postcode in the UK. The list must be ordered from north to south. Does not render anything, just gets unit tested.

Prerequisites
    Min Python 3.6
Dependencies
    Flask core

Setup:
    - Install Virtual environment
    - Navigate to project root folder
    - Create the environment "virtualenv env"
    - Activate the environment "source env/bin/activate"
    - Install the requirements "python -m pip install -r requirements.txt"

Run the app
    - export FLASK_APP=app
    - export FLASK_ENV=development
    - flask run
    - Navigate to http://127.0.0.1:5000/

Testing
    - from project root run "python -m unittest discover -v"

THIS IS AN OPEN SOURCE PROJECT - 0% GUARANTEE, USE IT AT YOUR OWN RISK ON YOUR PROJECTS.
IT IS A DEMO PROJECT TO SHOWCASE FLASK PROGRAMMING SKILLS
ALIGHT TO postcodes.io FOR PROPER USE OF API ENDPOINTS

