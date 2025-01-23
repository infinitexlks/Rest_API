# Flask REST API Example

This is a simple REST API built with Flask in Python that allows you to perform CRUD operations (Create, Read, Update, Delete) on a list of users.

## Features
- **GET** `/users`: Retrieve all users.
- **GET** `/users/<id>`: Retrieve a user by their ID.
- **POST** `/users`: Create a new user.
- **PUT** `/users/<id>`: Update an existing user.
- **DELETE** `/users/<id>`: Delete a user by their ID.

## Requirements
- Python 3.x
- Flask

## Setup

### Step 1: Install Dependencies

Before you can run the API, you need to install Flask. You can install it using `pip`:

```bash
pip install Flask
