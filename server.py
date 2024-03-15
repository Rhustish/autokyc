from fastapi import FastAPI
from ImageMatching.main import compare_faces_from_urls

app = FastAPI()

@app.get("/hc")
def healthcheck():
    return {"Hello":"World"}


@app.post("/imageComparison")
async def imageComparison(image1:str , image2 : str):
    return {"verified" : "1" if await compare_faces_from_urls(image1,image2) else "0" }

@app.post("/videoLive")
def videoLive():
    return 0