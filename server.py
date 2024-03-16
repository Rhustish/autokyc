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

@app.get("/hc",status_code=200)
def healthcheck():

    return "OK"


@app.post("/imageComparison",status_code=200)
async def imageComparison(image1:str , image2 : str):
    return "1" if await compare_faces_from_urls(image1,image2) else "0"

@app.post("/videoLive")
def videoLive():
    return 0
