mydiary

an application of an online diary

[![Build Status](https://travis-ci.com/ndyomugabi/mydiary.svg?branch=all_diary_entries)](https://travis-ci.com/ndyomugabi/mydiary)

[![Coverage Status](https://coveralls.io/repos/github/ndyomugabi/mydiary/badge.svg?branch=all_diary_entries)](https://coveralls.io/github/ndyomugabi/mydiary?branch=all_diary_entries)

[![Maintainability](https://api.codeclimate.com/v1/badges/6a47e2183dbf02f1e85d/maintainability)](https://codeclimate.com/github/ndyomugabi/mydiary/maintainability)


Features
get all diary entries
get specific diary entry
add an entry
modify an entry

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What you need to install the software and get started.

- git : to update and clone the repository
- python3: The base language used to develop the api
- pip: a python package used to install project requirements

Installation

Type:

The mydiary folder contains the system backend services.

To install the requirements, run:

Python A general purpose programming language

Pip A tool for installing python packages

Virtualenv A tool to create isolated Python environments

Development setup
Create a virtual environment and activate it
 virtualenv venv
 .\venv\Scripts\activate.bat
Install dependencies
pip3 install -r requirements.txt
Run the application
cd mydiary
python run.py

Now you can access the system api Endpoints:



Running the tests
To run the tests, run the following commands
pytest --cov=.

Built With
Flask - The web framework used
Python - Framework language

Authors
Ndyomugabi Esther - - ndyomugabi

Acknowledgments
Andela Development Uganda