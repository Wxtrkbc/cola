import asyncio

from cola.router.routers import BaseRouter
from .server import Server
from .request import Request


# def run_app(host='127.0.0.1', port=8080, ssl=None, backlog=100):
#     loop = asyncio.get_event_loop()
#     server = loop.create_server(host, port, ssl=ssl, backlog=backlog)
#     loop.run_until_complete(server)
#     loop.run_forever()


class Application(object):

    def __init__(self, loop=None, router=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        if router is None:
            router = BaseRouter()

        self._loop = loop
        self._router = router

    @property
    def router(self):
        return self._router

    @property
    def loop(self):
        return self._loop

    def _make_request(self, message, payload, protocol, _cls=Request):
        return _cls(message, payload, protocol)

    def make_handler(self, *args, **kwargs):
        return Server(self._handle, request=self._make_request, loop=self.loop, **kwargs)

    async def _handle(self, request):
        handler = await self._router.resolve(request)
        resp = await handler(request)
        return resp



