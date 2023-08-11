from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import find

app = FastAPI(
    title="metro",
    description="Веб-сервис для test'a",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "find",
            "description": "Операции с поиском по таблице find",
        }
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(find.router)
