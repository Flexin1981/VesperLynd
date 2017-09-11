

class ResponseInterface(object):

    def render(self):
        raise NotImplementedError("respnse must implement the render method.")