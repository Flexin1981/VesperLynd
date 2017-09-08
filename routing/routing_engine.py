from interface import RoutingInterface
import re


class RoutingEngine(RoutingInterface):

    def __init__(self):
        self.routes = []

    def match_route(self, host, uri):
        """
            Return the callable that matches the incoming host and uri pattern
        :param host:
        :param uri:
        :return:
        """
        for route in self.routes:
            if route.is_match(host):
                host = route

        if host:
            for route in host.uris:
                if route.is_match(uri):
                    return route.callable

        return None

    def append(self, route):
        if not isinstance(route, HostRoute):
            raise ValueError('top level routes must be host based routes')
        self.routes.append(route)


class HostRoute(object):

    def __init__(self, host, uri_routes):
        self.host = host
        self.uris = uri_routes

    def is_match(self, host):
        if re.match(self.host, host):
            return True
        return False


class UriRoute(object):

    def __init__(self, uri, callable):
        self.uri = uri
        self.callable = callable

    def is_match(self, uri):
        if re.match(self.uri, uri):
            return True
        return False
