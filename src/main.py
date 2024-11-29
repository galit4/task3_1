from fastapi import FastAPI
from api import info, getall, getallv2

app = FastAPI()
app.include_router(info.router)
app.include_router(getall.router)
app.include_router(getallv2.router)
