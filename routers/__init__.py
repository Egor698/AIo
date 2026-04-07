from fastapi import FastAPI
from routers.book import router as book_router

def include_routers(app: FastAPI):
    app.include_router(book_router)