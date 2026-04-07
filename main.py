import uvicorn
from fastapi import FastAPI

import routers

app = FastAPI(
    title='Приложение Библиотека'
)


routers.include_routers(app)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8800, workers=4)