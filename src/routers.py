from fastapi import APIRouter

route1 = APIRouter()
route2 = APIRouter()


@route1.get('/something')
async def endpoint1():
    return 42


@route2.get('/something')
async def endpoint2():
    return 42
