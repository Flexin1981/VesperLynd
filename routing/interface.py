from abc import ABCMeta, abstractmethod


class RoutingInterface(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def match_route(self, host, uri):
        """
            The match_route method must interogate the routing structure with the goal of returning the callable that
            will handle the view functionality of the api.
        :param host:
        :param uri:
        :return: callable or None
        """
        raise NotImplementedError("route matching method not implimented")
