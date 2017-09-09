

class Response(object):

    def calculate_content_length(self):
        return str(len(self.body))

    def __init__(self):

        self.status = None
        self.headers = []
        self.body = None

    def render(self):
        pass