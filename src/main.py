import uvicorn
from fastapi import FastAPI

from internal_app import internal_app
from routers import route1

app = FastAPI()

app.mount('/internal', internal_app)
app.include_router(route1, prefix='/route1')


if __name__ == '__main__':
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)
