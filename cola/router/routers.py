

class BaseRouter(object):
    def __init__(self):
        self._router = {}

    def resolve(self, request):
        method = request.method
        raw_path = request.rel_url.raw_path
        if raw_path not in self._router:
            raise ValueError("Not found URL match")
        return self._router[raw_path]

    def add_router(self, method, path, handler, name=None):
        # todo complete router
        self._router[path] = handler

