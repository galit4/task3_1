from fastapi import FastAPI
from api import getallv2, info, getnew, getknown, getkey, get_all
#імпортуєм фастапі та модулі з ендпоінтами

app = FastAPI()#робимо еземпляр класу для зручності
app.include_router(info.router)#додаємо роутери з кожним ендпоінтом
app.include_router(getallv2.router)
app.include_router(get_all.router)
app.include_router(getnew.router)
app.include_router(getknown.router)
app.include_router(getkey.router)