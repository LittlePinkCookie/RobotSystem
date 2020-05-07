from aiohttp import web

from server.server import Server

if __name__ == '__main__':
    server = Server()
    web.run_app(server.app)