

class Request(object):

    def __init__(self, environ):
        """
            http request object.
        :param environ:
        """
        [self.__setattr__(name, val) for name, val in environ.items()]
