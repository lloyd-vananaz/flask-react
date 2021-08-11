# Research - Flask and React App

## How To Run Apps

Make sure you have done the first time setup on each app. Follow the README files inside the `api` and `react-app` folders first.

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
5. Run flask `flask run`
6. Open browser and enter http://localhost:3030