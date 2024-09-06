from fastapi import FastAPI

app = FastAPI()

app.get('/')
def home():
    return{'data':'welcome to Home Page'}


app.get('/contact')
def home():
    return{'data':'welcome to contact Page'}


import uvicorn
uvicorn.run(app)