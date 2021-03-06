<img src="https://github.com/zachvance/flask_boilerplate/blob/main/images/banner.png" alt="Banner" width="1000"/>

# Flask Boilerplate
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A basic flask boilerplate for personal projects.

## Features
- Premade templates and routing for Home, Blog, About, Signup, Login and Logout pages.
- A Protected page (must be logged in to view).
- An Admin page (must be both logged in and have 'admin' in permissions to view).
- CSS styling for all of the above included.
- Preset connection to a database - either Postgres or SQLite, with SQLite being the default. This can be changed in the 'connections.py' file.
- A basic SQLite database with a 'users' table.
- A 'User' class that utilizes the database info via SQLAlchemy.

## Images

<img src="https://github.com/zachvance/flask_boilerplate/blob/main/images/login_page.png" alt="Login Page" width="1000"/>

<img src="https://github.com/zachvance/flask_boilerplate/blob/main/images/home_page.png" alt="Home Page" width="1000"/>


## Background
I wanted my own boilerplate for some of the aspects/features I find myself setting up most frequently on small scale web apps. This gives me a clean template to work off that could be modified and ready to demo relatively quickly, along with a local database for testing and styling already taken care of.

Additionally, it's been a good exercise in organization; sometimes taking a step back and working on a smaller scale project allows you to structure things differently and improve your fundamentals, which can be applied to larger undertakings.

## Usage
### Default logins

The default logins that come contained within the 'database.sqlite3' file are 'user1@example.com' and 'admin@example.com'.
The passwords for these logins are 'user1' and 'admin', respectively.

## Todo
- Clean up the CSS classes.
- Possibly add a settings/user profile management page.
