import asyncio

from .protocol import ServerHttpProtocol


class RequestHandler(ServerHttpProtocol):

    def __init__(self, server, **kwargs):

        self._server = server
        self._handler = server.handler
        self._request = server.request

    def connection_made(self, transport):
        super().connection_made(transport)
        self._server.connection_made(self, transport)

    def connection_lost(self, exc):
        self._server.connection_lost(self, exc)

        super().connection_lost(exc)
        self._request = None
        self._server = None
        self._handler = None

    async def handle_request(self, message, payload):
        self._server.request_count += 1
        request = self._request(message, payload, self)

        try:
            resp = await self._handler(request)
        except Exception as exc:
            pass


class Server(object):

    def __init__(self, handler, request=None, loop=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()

        self._handler = handler
        self._request = request
        self._loop = loop
        self._kwargs = kwargs
        self._request_count = 0

        self._connection = {}

    def __call__(self):
        return RequestHandler(self, loop=self._loop, **self._kwargs)

    @property
    def handler(self):
        return self._handler

    @property
    def request_factory(self):
        return self._request

    def connection_made(self, handler, transport):
        self._connection[handler] = transport

    def connection_lost(self, handler, exc=None):
        if handler in self._connections:
            del self._connection

