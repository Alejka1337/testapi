# ShortLinker

### You can see how the project works [Here](http://139.59.141.234:8000/)

## How to launch a project?

- ####  Create and activate virtual environment

`python3 -m venv venv`

`source venv/bin/activate`

- #### Download the project from the repository

`git clone https://github.com/Alejka1337/testapi.git`

- #### Install the dependencies from the requirements.txt file with the command:

`pip install -r requirements.txt`

- #### Create database migrations

`python3 manage.py migrate`

- #### Run application on local server

`python3 manage.py runserver`

## Working with the web version

- #### At http://localhost:8000 in the input field, paste the URL to get the shorlink
- #### After reloading the page, get a shorlink
- #### Go to http://localhost:8000/shorlink and the server will redirect you to the URL


## Working with the API

- #### Make a POST request to `http://localhost:8000/api/create-shortlink/` and pass the "url" parameter in the request body to get the shortlink

- #### Make a GET request to `http://localhost:8000/api/shortlink/detail/id` for view shortlink click statistics.__You must be the shortlink creator to see the stats.__

- #### Make a PUT request to `http://localhost:8000/api/shortlink/update/id` for remove shortlink (no parameters need to be passed)

- #### Make a POST request to `http://localhost:8000/api-token-auth/` for get the authorization code (it is necessary to pass the "username", "password" and "email" parameters in the request body). __You can use the token when making API requests by passing the `Authorization` parameter to the headers with the value `token your_token`.__


