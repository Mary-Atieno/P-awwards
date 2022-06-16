# project name

## Project-Awwards

## Author

Mary Atieno

## Description

A website application where users can view and rate projects made by other users.

## Installation

To view the app.Visit

Clone this repo: git clone [here](https://github.com/Mary-Atieno/project-awwards.git)

The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

open your terminal and navigate to projects then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

To run the app, you'll have to run the following commands in your terminal

       pip install -r requirements.txt

On your terminal,Create database awwards using the command below.

       CREATE DATABASE projects; 
       **if you opt to use your own database name, replace projects with your preferred name, then also update settings.py variable DATABASES > NAME

Migrate the database using the command below

       python3 manage.py migrate

Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

       python manage.py runserver

Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Technologies used

* Python 3.8.10
* Django
* Postgresql

## User Story

Users need to Sign in to the application to post projects and review projects.

Users can view different projects and their details.

Users can post a project to be rated/viewed.

Users can search for different projects.

Users can view projects overall score.

Users can view their profile page with all their published projects.

Users can rate/review other users' projects.

## License

## MIT License

Copyright (c) 2022 Mary Atieno

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
