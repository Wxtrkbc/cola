from aiohttp import web


async def hello(request):
    return web.json_response({'name': 'Jason'})


app = web.Application()
app.router.add_get('/', hello)

web.run_app(app)


# from cola.web import app
# from cola.web.response import json_response
#
# async def hello(request):
#     return json_response(data={'name': 'Jason'})
#
#
# web = app.Application()
# web.router.add_router('get', '/', hello)
#
# app.run_app(web)

