import unittest
from routing.routing_engine import RoutingEngine, HostRoute, UriRoute
from views.api_view import ApiView


class MockView(ApiView):

    def get(self):
        return True


class TestRoutingEngineInstantiation(unittest.TestCase):

    def test_routing_engine_raises_value_error_when_non_host_route_given(self):
        with self.assertRaises(ValueError):
            self.engine = RoutingEngine()
            self.engine.append("")


class TestRoutingEngineMethods(unittest.TestCase):

    def test_match_route_returns_view(self):
        self.engine = RoutingEngine()

        self.engine.append(
            HostRoute(
                "localhost:8080", [UriRoute("/route",  MockView())]
            )
        )

        self.assertIsInstance(self.engine.match_route("localhost:8080", "/route"), ApiView)