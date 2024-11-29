from fastapi import FastAPI
from api import info, getall, getallv2, getnew, getknown, getkey

app = FastAPI()
app.include_router(info.router)
app.include_router(getall.router)
app.include_router(getallv2.router)
app.include_router(getnew.router)
app.include_router(getknown.router)
app.include_router(getkey.router)