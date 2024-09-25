## Description This is a simple Flask web application with user authentication using Firebase Authentication. It allows users to register, login, view their profile, and logout. The application ensures a no-cache policy for secure user sessions.

## Features - Frontend HTML/CSS with navbar, subnav, footer, Main content {Excercise 1} - For Backend it using Flask for python server creation { Excercise 2} - Dynamic content showing Date in top {Excercise 3} - User registration with name, phone, email, and password {Exercise 4} - User login and logout functionality - Session-based user authentication - Profile page to display user information {Exercise 5} - No-cache policy implementation for secure sessions

## Installation 1. Clone the Repository: - Clone or download the repository from [GitHub](https://github.com/Aman0818/Full-Stack-With-Flask.git). 2. Install Dependencies: - Make sure you have Python installed. Then install the required Python packages using pip. 
``` pip install Flask Flask-Bcrypt python-dotenv functools Pyrebase Pyrebase4 ``` 

3. Run the Application: - Start the Flask server to run the API.
``` python App.py ```

- The API server will start running locally at `http://127.0.0.1:8000`.

### API Endpoint
- Endpoint: `/`
- Method: `GET` - Endpoint: `/register`
- Method: `GET, POST` - Endpoint: `/login`
- Method: `GET, POST` - Endpoint: `/profile`
- Method: `GET`
### Demo User - emial ID: `demo@gmail.com` - passwor: `demopass`
