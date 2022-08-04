# Library (Czytelnia) Backend

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)

<!-- * [License](#license) -->

## General Information

Backend application for a free book library. 
Application exposes REST API for use for frontend apps.
This application is supposed to work in conjcution with\
android frontend app: https://github.com/AdKowalewski/Czytelnia.

## Technologies Used

- Python - version 3.9.7
- Django - version 3.2.4
- Django Ninja - version 0.16.1

## Features

- user validation and authorization using JWT
- create account, browse books
- add books to favorites, list your favorites
- rate books, write book reviews
- get cover and pdf for given book
- add new books via django admin panel
- swagger ui at /api/docs

## Setup
To run  you need python installed. All project dependencies are listed in requirements.txt.
To install all deps run:\
`pip install -r requirements.txt`\
To start server run:\
`python manage.py runserver`

