from fastapi import FastAPI,Response
from ImageMatching.main import compare_faces_from_urls

app = FastAPI()

@app.get("/hc")
def healthcheck():
    return {"Hello":"World"}


@app.post("/imageComparison")
async def imageComparison(image1:str , image2 : str):
    verified = "1" if await compare_faces_from_urls(image1,image2) else "0"
    return Response(content={"verified": verified}, status_code=200)

@app.post("/videoLive")
def videoLive():
    return 0