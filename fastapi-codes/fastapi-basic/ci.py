'''
Simple test fastapi application for testing Github Actions to realize
continuous integration (CI). 

path: .github/workflows/xxx.yaml
'''
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}
