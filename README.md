# FastAPI Template

This is a ready to go FastAPI template with a decent project folder structure.<br/>


## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
Create a new python environment
```
python -m venv env
```

Activate the environment
```
env\Scripts\activate
```

You should first install all the dependency libraries by running the following command
```
python setup.py
```

## Running the FastAPI Application
Running the follwing command will serve the API at this URL: http://127.0.0.1:8000
```
uvicorn main:app --reload
```

## Documentation
FastAPI provides two different types of API Documentation
1. Swagger API Documentation: http://127.0.0.1:8000/docs
2. Redocs API Documentation: http://127.0.0.1:8000/redoc