from aiohttp import web


async def hello(request):
    return web.json_response({'name': 'Jason'})


app = web.Application()
app.router.add_get('/', hello)

web.run_app(app)
