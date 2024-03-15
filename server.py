from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from ImageMatching.main import compare_faces_from_urls



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/hc")
def healthcheck():
    return Response(content={"HealthCheck":"OK"}, status_code=200)


@app.post("/imageComparison")
async def imageComparison(image1:str , image2 : str):
    verified = "1" if await compare_faces_from_urls(image1,image2) else "0"
    return Response(content={"verified": verified}, status_code=200)

@app.post("/videoLive")
def videoLive():
    return 0
