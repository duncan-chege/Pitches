# Pitch & Win

This is a flask application used to accept and display user pitches in different industries 

## Author Information
Written by *Duncan Chege*. My first attempt at interating psql into my flask app

## Installation

## Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Pip install the dependencies from the requirements file
4. Rename the postgresql database username and password from config.py to be your own
5. App instance in manage.py should be under development not production if you're changing the database schema
6. Create a database called bookmodel
7. Carry out migrations
8. Run the server using ./start.sh terminal command

## Behaviour Driven Development

| Behavior our program should handle | Input description |  Output description
| --- | --- | --- |
| `Click on a button to view different pitches` | None | Pitches displayed
| `Registration into the app` | User credentials |  Redirection to login form
| `View individual pitches` | Pitches in separate form |  A list of pitches
| `Submission of pitches` | Pitches in user defined categories |  A list of pitches
| `View different categories` | None |  A list of categories and their pitches

### Contact Information

To reach me, email me at: > dshege4@gmail.com


### License

-This project is licensed under the terms of the [MIT license](https://github.com/dunyung1/Web-work/blob/master/MIT%20License)
