from interface import ApiInterface


class ApiView(ApiInterface):

    METHOD_MAP = {
        "CONNECT": "connect", "DELETE": "delete", "GET": 'get', "HEAD":"head", "OPTIONS": "options", "PATCH": "patch",
        "POST": "post", "PUT": "put"
    }

    def __getattr__(self, item):
        return self.__getattribute__(self.METHOD_MAP[item])