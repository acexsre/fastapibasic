from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"msg": "Ayush's BasicXFastAPI App"}

@app.get("/health")
def read_health():
    return {"HealthCheck": "Working"}

@app.get("/bot/{bot_id}")
def read_item(bot_id: int, q: Union[str, None] = None):
    return {"botID": bot_id, "q": q}
