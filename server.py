from fastapi import FastAPI
from ImageText.main import compare_faces_from_urls

app = FastAPI()

@app.get("/hc")
def healthcheck():
    return {"Hello":"World"}

@app.post("/imageToText")
def imageToText(image:str):
    return 0

@app.post("/imageComparison")
def imageComparison(image1:str , image2 : str):
    return {"verified" : "1" if compare_faces_from_urls(image1,image2) else "0" }

@app.post("/videoLive")
def videoLive():
    return 0