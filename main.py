from fastapi import FastAPI

from users.routers import router

app = FastAPI()

app.include_router(router=router, prefix="/task_2")


@app.get("/")
async def root():
    return {"message": "Hello World"}
