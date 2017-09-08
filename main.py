from app.wsgi_app import WsgiApp as app





if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8081, app())
    srv.serve_forever()