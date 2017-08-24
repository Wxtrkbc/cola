import json
from multidict import CIMultiDict, CIMultiDictProxy


class StreamResponse(object):
    def __init__(self, status=200, headers=None):
        pass

    def set_status(self, status):
        self._status = int(status)


class Response(StreamResponse):
    def __init__(self, status=200, text=None, headers=None, content_type=None, body=None,
                 charset=None):
        if headers is None:
            headers = CIMultiDict()
        elif not isinstance(headers, (CIMultiDict, CIMultiDictProxy)):
            headers = CIMultiDict(headers)

        if not isinstance(text, str):
            raise TypeError("text argument must be str ({})".format(type(text)))

        if content_type is None:
            content_type = 'text/plain'

        if charset is None:
            charset = 'utf-8'

        headers['Content-Type'] = (content_type + '; charset=' + charset)
        body = text.encode(charset)
        self.body = body


def json_response(data=None, status=200, headers=None, content_type="application/json"):
    text = json.dumps(data)
    return Response(status=status, text=text, headers=headers, content_type=content_type)
