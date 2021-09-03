# Python Research: Flask and React App

We need to install Python first before we can have Flask.

## Python: Installation
1. Check if you have python installed already by entering `python` in you terminal.
2. If you need to install Python, you may download it in the [Download Python Page](https://www.python.org/downloads/).

## Python: Using REPL (Read-Evaluate-Print-Loop)

1. Enter `python3` in terminal.
2. Start coding!

## Python: Running From File

1. Start terminal.
2. Enter `python3 <path/filename.py>`

## Quick Demo

There is a quick demo available in this repository.

### Python Basics/Advanced

You can quickly run the following files with `python3 .\demo\mutability.py`

- [mutability.py](demo/mutability.py)
- [error_handling.py](demo/error_handling.py)
- [unit_testing.py](demo/unit_testing.py)

### Flask Demo Apps

1. Start a terminal in the `demo/flask` directory.
2. Create a virtual environment and activate it.
   - Windows
      ```
      > python3 -m venv venv
      > venv\Scripts\activate
      ```
   - MacOS/Linux
      ```
      > python3 -m venv venv
      > . venv/bin/activate
      ```
3. Once the virtual environment is activated, install the following using `pip`:
   ```
   pip install flask flask-sqlalchemy pymysql
   ```
4. Set the environment variables. You can change **"shows"** to **"todo"** if you want to run the todo.py instead.
   - Windows
      ```
      > $env:FLASK_APP = "shows"
      > $env:FLASK_ENV = "development"
      ```
   - MacOS/Linux
      ```
      > export FLASK_APP=shows
      > export FLASK_ENV=development
      ```
5. You will need a working MySQL database to run the `todo.py`. For `shows.py` you can skip this step. Setup MySQL and run the scripts found in the `mysql-scripts\1_create_db_table.sql` and update the database connections string username, password, hostname and database name.
6. Run flask. You may or may not set the hostname and port.
   ```
   > flask run -h localhost -p 3030
   ```

## How To Run Flask API and React App

Make sure you have done the first time setup on each app.

- [First Time Setup for Flask](api/README.md)
- [First Time Setup for React](react-app/README.md)

### Running Flask and React App Separately

Note: Token based authentication doesn't seem to be working when using this approach due to cookies not in the same port. Please use the other approach, 'Running Flask And React As One' to test authentication or you may comment out the `@jwt_required()` decorators in the routes so you will not need to login.

1. Start a terminal.
2. Navigate to `api` directory.
3. Enter the following
   ```
   > venv/Scripts/activate
   > flask run
   ```
4. Open another terminal. Don't use the same as the previous.
5. Enter `npm start`

### Running Flask and React As One

1. Start a terminal.
2. Navigate to the React App folder.
3. Build the react app `npm run build`.
4. Navigate to the Flask API folder.
5. Run flask by entering `flask run`
6. Open browser and enter http://localhost:3030