[![Build Status](https://travis-ci.org/ankcode/politico-api.svg?branch=develop)](https://travis-ci.org/ankcode/politico-api)
# politico app

Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.

# politico-api
politico app APIs

This contains tha APIs for the politico app.
The following are the set of API endpoints for the politico app in this repo:

1. Create a political party.
2. Get all political parties.
3. Get a specific political party.
4. Edit a specific political party.
5. Delete a particular party.
6. Create a political office.
7. Get all political offices.
8. Get a specific political office.

## API Endpoints

| Method        | Endpoints                       |Specifications                              |
| ------------- |:-------------------------------:|--------------------------------------------|
| POST          | api/v1/parties                  |Create a political party.                   |
| GET           | api/v1/parties/party-id    |Fetch a specific political party record.    |
| GET           | api/v1/parties                  |Fetch all political parties records.        |
| PATCH         | api/v1/parties/party-id/name  |Edit the name of a specific political party.|
| DELETE          | api/v1/parties/party-id       |Delete a specific political party.    |
| POST           | api/v1/offices                  |Create a political office.        |
| GET        | api/v1/offices  |Fetch all political offices records.|
| GET          | api/v1/offices/party-id       |Fetch a specific political office record.   |

## How to install and run the endpoints.

1. Clone the politico-api repo: 
    `https://github.com/ankcode/politico-api.git`:

2. Create a virtual environment for your app by running the following command in your terminal:

    `virtualenv my-env`

3. activate virtual environment

    `source my-env\bin\activate`

4. Install the required dependencies from the requirements.txt file

    ` pip3 install -r requirements.txt`

5. To run the application:

    `export FLASK_APP = run.py`
    `export MODE = development`
    `flask run`

## Relevant pivotal tracker stories
[Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2245508)


