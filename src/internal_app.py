from fastapi import FastAPI

from routers import route2

internal_app = FastAPI()
internal_app.include_router(route2, prefix='/route2')
