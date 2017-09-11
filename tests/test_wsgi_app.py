import unittest
from app.wsgi_app import WsgiApp


class TestWsgiAppInstantiation(unittest.TestCase):

    def setUp(self):
        self.app = WsgiApp()

    def test_wsgi_instantiate_without_routing_adds_default_engine(self):
        from routing.routing_engine import RoutingEngine
        self.assertEquals(type(self.app.routing), RoutingEngine)

    def test_wsgi_app_raises_error_when_routing_engine_does_not_impliment_interface(self):
        with self.assertRaises(TypeError):
            self.app = WsgiApp("")
