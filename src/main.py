from fastapi import FastAPI
from src.resource.user.api import user_router
from src.resource.admin.api import data_router

from src.resource.auth.api import auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(data_router)



