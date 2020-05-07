from aiohttp import web

from config_reader import config
from server.server import Server

if __name__ == '__main__':
    server = Server()
    web.run_app(app=server.app, port=int(config.get_param("server.port", 5000)))
