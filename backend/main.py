from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="PDF Data Manager API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
