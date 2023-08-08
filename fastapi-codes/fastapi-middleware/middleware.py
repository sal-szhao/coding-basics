from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

'''
Middleware essentially is the mechanism that allows users to modify the requests and responses.
'''

app = FastAPI()

'''
You can add code to be run with the request, before any path operation receives it.
And also after the response is generated, before returning it.
The following code will add process tiem to the response header.
'''
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


'''
Origins specify what URLS can send requests to the backend application.
Eg. If the http-server is running at "http://127.0.0.1:8080",
trying to fetch "http://127.0.0.1:8000/middle", is not allowed.

Run the command `http-server` to start the local http service.
'''
origins = [
    "http://localhost",
    "http://localhost:8080",
    # "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/middle')
async def middle():
    return {"message": "Hello World"}
