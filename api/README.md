# Todo Flask API

## Python Installation
1. Check if you have python installed already by entering `python` in you terminal.
2. If you need to install Python, you may download it in the [Download Python Page](https://www.python.org/downloads/).

## Using REPL (Read-Evaluate-Print-Loop)

1. Enter `python3` in terminal.
2. Start coding!

## Running from file

1. Start terminal.
2. Enter `python3 <path/filename.py>`. Example: `python3 ./python-basics/1-numbers.py`.

## First Time Setup for Flask

1. Start terminal in this directory.
2. Create a virtual environment by entering `python3 -m venv venv`.
3. Activate the virtual environment `venv/Scripts/activate`.
4. Install dependencies `pip install .`.

## Using MySQL

1. Install MySQL in your local machine.
2. Create a database and tables by running the scripts from the `mysql` folder in the root directory.
3. Create `.env` file in this directory and add the following:
    ```
    TODODB_HOST=localhost
    TODODB_NAME=database-here
    TODODB_USER=user-here
    TODODB_PWD=password-here
    ```

## Using SQLite

You can use SQLite as your database but you have to initialize it first.

1. Toggle comment on the following code:
    - setup.py (You might have to do `pip install .` again after this change)
        ```
        # 'Flask-Migrate==3.0.1'
        ```
    - app\\\_\_init\_\_.py
        ```
        # from flask_migrate import Migrate
        # migrate = Migrate()
        # migrate.init_app(app, db)
        ```
    - config.py
        ```
        SQLALCHEMY_DATABASE_URI = db_connection_string # For MySQL
        # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # For SQLite
        ```
2. Start terminal in this directory.
3. Activate the virtual environment `venv/Scripts/activate` and enter the following:
    ```
    > flask db init
    > flask db migrate -m "task table"
    > flask db upgrade
    ```
4. This will add additional folders and files.

## Test Database Connection

1. Start terminal in this directory.
2. Activate the virtual environment `venv/Scripts/activate`.
3. Enter `flask shell`.
4. Try entering `db`. If no error is displayed then you are good to go.