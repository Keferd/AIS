import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application.routes import router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)      # подключаем обработчик API URI

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
