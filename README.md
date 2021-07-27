# Python

## Installation
1. Check if you have python installed already by entering `python` in you terminal/command line/PowerShell.
2. If you need to install Python, you may download it in the [Download Python Page](https://www.python.org/downloads/).

## Using REPL (Read-Evaluate-Print-Loop)

1. Enter `python3` in terminal/command line/PowerShell.
2. Start coding!

## Running from file

1. Start terminal/command line/PowerShell.
2. Enter `python3 <path/filename.py>`. Example: `python3 ./python-basics/1-numbers.py` to run `1-numbers.py` in this repository.

## First Time Setup for Flask

1. Start terminal/command prompt.
2. Navigate to the `api` directory.
3. Create a virtual environment by entering `python3 -m venv venv`.
4. Activate the virtual environment `venv/Scripts/activate`.
5. Install dependencies `pip install .`.

## First Time Setup for React

1. Start terminal/command prompt.
2. Navigate to `shows-app` directory.
3. Install dependencies `npm install`.

## How To Run Apps

### Running Flask and React App Separately

1. Start a terminal/command prompt.
2. Navigate to `api` directory.
3. Enter the following
   ```
   > venv/Scripts/activate
   > $env:FLASK_APP = "flaskr"
   > $env:FLASK_ENV = "development"
   > flask run -h localhost -p 3030
   ```
4. Open another terminal/command promt. Don't use the same as the previous.
5. Navigate to `shows-app` directory
6. Enter `npm start`
