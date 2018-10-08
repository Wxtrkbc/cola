from yarl import URL


class BaseRequest(object):
    def __init__(self, message, payload, protocol):
        self._message = message
        self._payload = payload
        self._protocol = protocol

        self._transport = protocol.transport
        self._reader = protocol.transport
        self._writer = protocol.writer
        self._time_service = protocol.time_service
        self._task = protocol._request_handler

    @property
    def task(self):
        return self._task

    def method(self):
        return self._message.method

    def rel_url(self):
        url = URL(self._message.path)
        if self._message.path.startwith('//'):
            return url.with_path(self._message.path.split('?')[0])
        return url

    def url(self):
        return URL('http://{}{}'.format(self._message.headers.get('HOST'),
                                        str(self.rel_url)))


class Request(BaseRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mach = None

    def app(self):
        return self._match.apps[-1]
