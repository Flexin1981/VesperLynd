import json
from routing.interface import RoutingInterface
from routing.routing_engine import RoutingEngine
from http.request import Request


class WsgiApp(object):

    def set_routing_engine(self, engine):
        if engine is None:
            self.routing = RoutingEngine()
        else:
            if not isinstance(engine, RoutingInterface):
                raise TypeError("routing engine must impliment routing interface")
            self.routing = engine

    def __init__(self, routing_engine=None):
        self.set_routing_engine(routing_engine)

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self.routing.match_route(request.HTTP_HOST, request.PATH_INFO)
        response_obj = view.__getattr__(request.REQUEST_METHOD)(request)
        response = response_obj.render()

        start_response(response.status, response.headers)

        return response.body
