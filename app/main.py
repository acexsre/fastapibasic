from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Ayush's BasicXFastAPI App"}

@app.get("/health")
def read_health():
    return {"HealthCheck": "Working"}

@app.get("/bot/{bot_id}")
def read_item(bot_id: int, q: Union[str, None] = None):
    return {"botID": bot_id, "q": q}
