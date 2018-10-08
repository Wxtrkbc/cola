
class Request(object):

    def __init__(self, message, payload, protocol):
        self._message = message
        self._payload = payload
        self._protocol = protocol
