from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {
        'name': "Chetan"
    }}


@app.get('/about')
def about():
    return {'data': 'about details'}
