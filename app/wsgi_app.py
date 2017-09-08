import json
from routing.interface import RoutingInterface
from routing.routing_engine import RoutingEngine


class WsgiApp(object):

    def set_routing_engine(self, engine):
        if not engine:
            self.routing = RoutingEngine()
        if not isinstance(engine, RoutingInterface):
            raise TypeError("routing engine must impliment routing interface")
        self.routing = engine

    def __init__(self, routing_engine=None):
        self.set_routing_engine(routing_engine)

    def __call__(self, environ, start_response):

        view = self.routing.match_route(environ['HTTP_HOST'], environ['PATH_INFO'])

        start_response(
            '200 OK',
            [('Content-Type', 'application/json')]
        )
        return view.__getattr__(environ['REQUEST_METHOD'])()

