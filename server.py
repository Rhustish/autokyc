from fastapi import FastAPI

app = FastAPI()

@app.get("/hc")
def healthcheck():
    return {"Hello":"World"}

@app.post("/imageToText")
def imageToText(imageToText):
    return 0

@app.post("/imageComparison")
def imageComparison():
    return 0

@app.post("/videoLive")
def videoLive():
    return 0