from fastapi import FastAPI
from api import info, getall, getallv2, getnew, getknown, getkey
#імпортуєм фастапі та модулі з ендпоінтами

app = FastAPI()#робимо еземпляр класу для зручності
app.include_router(info.router)#додаємо роутери з кожним ендпоінтом
app.include_router(getall.router)
app.include_router(getallv2.router)
app.include_router(getnew.router)
app.include_router(getknown.router)
app.include_router(getkey.router)