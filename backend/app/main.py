from fastapi import FastAPI

app = FastAPI(title="Car Wash API")


@app.get("/")
async def root():
    return {"message": "Car wash API is running"}