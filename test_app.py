from app.wsgi_app import WsgiApp
from routing.routing_engine import RoutingEngine, HostRoute, UriRoute
from views.api_view import ApiView
from http.response import Response


def welcome():
    return '{"this": "that"}'


def working_routing():
    return '{"working": "routing"}'

def working_routing2():
    return '{"working2": "routing2"}'


class View(ApiView):

    def get(self, request):
        response = Response()

        response.status = "200 OK"
        response.body = '{"class": "view"}'
        response.headers = [("Content-Type", "application/json")]
        return response


routing = RoutingEngine()
routing.append(
    HostRoute(
        'localhost:8081',
        [
            UriRoute('/.+/that', View()),
            UriRoute('/this', working_routing),
            UriRoute('/', welcome)
        ]
    )
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8081, WsgiApp(routing_engine=routing))
    srv.serve_forever()
