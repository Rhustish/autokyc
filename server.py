from fastapi import FastAPI

app = FastAPI()

@app.get("/hc")
def healthcheck():
    return {"Hello":"World"}

@app.post("/imageToText")
def imageToText(image:str):
    return 0

@app.post("/imageComparison")
def imageComparison(image1:str , image2 : str):
    return 0

@app.post("/videoLive")
def videoLive():
    return 0