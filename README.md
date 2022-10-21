# dAIzy-API

## Intro
FastAPI application - https://fastapi.tiangolo.com/

## Installation
#### Create Environment
`python -m venv env`

#### Activate Environment
if Windows: `env\Scripts\activate`  <br/>
if Ubuntu: `source env/bin/activate`

#### Installing requirements
`pip install -r requirements.txt`

#### Run the server
`start_server.bat`
or
`uvicorn main:app`

## Test Suite

### Run test
`pytest test`

### Run Coverage
`coverage run -m pytest`

### Generate HTML report
`coverage html` <br/>
Open htmlcov/index.html

## Project Contents
- `/docs` - Contains Architecture Diagrams, ER-Diagrams etc
- `/resources` - Contains resource files (.json, .xlsx, .csv etc)
