# minotes

## Description of the web application
Mi-Notes is a simple note-taking web application built with Django. The app allows users to create, view, and delete notes, as well as delete all notes at once.

## Usage
To use the app, simply go to https://minotes7.herokuapp.com/ in your web browser. You will be greeted with a login page where you can either create a new account or log in with an existing account.

Once you are logged in, you will be taken to the main notes page. Here, you can create new notes by entering a title and content for the note, and clicking the "Add Note" button. You can also view your existing notes and delete them individually or all at once.

## Installation
### Using docker:
* Clone the repository: git clone https://github.com/Nhlosokuhle/minotes.git
* Navigate to the project directory: cd minotes
* MAKE SURE THAT DOCKER DESKTOP IS OPENED
* Build the Docker image: docker build -t minotes .
* Run the Docker container: docker run -p 8000:8000 minotes
* After following the installation instructions, you should be able to access the Django project by navigating to http://localhost:8000 in your web browser. From there, you can create the account and access the menu.

### On your pc:
* Clone the repository: git clone https://github.com/Nhlosokuhle/minotes.git
* Navigate to the project directory: cd minotes
* Run the following command: py managr.py runserver
* After following the installation instructions, you should be able to access the Django project by navigating to http://localhost:8000 in your web browser.

The application is available online at https://minotes7.herokuapp.com/

## Author(s)
Nhlosokuhle Bandile Khoza
