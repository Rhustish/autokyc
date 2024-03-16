from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from ImageMatching.main import compare_faces_from_urls
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

temp = 6

@app.get("/hc",status_code=200)
def healthcheck():

    return "OK"


@app.get("/imageComparison",status_code=200)
def imageComparison():
    global temp
    temp+=1
    return temp%2
    

@app.post("/videoLive")
def videoLive():
    return 0
