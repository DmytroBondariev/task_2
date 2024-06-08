from fastapi import FastAPI

from users.routers import router
from auth.routers import router as auth_router

app = FastAPI()

app.include_router(router=router, prefix="/task_2")
app.include_router(router=auth_router, prefix="/task_2")


@app.get("/")
async def root():
    return {"message": "Hello World"}
