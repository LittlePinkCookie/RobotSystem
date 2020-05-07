from aiohttp import web

import socketio

from config_reader import config
from server.utils import authenticate_controller
from system import camera

debug_mode = config.get_param("server.debug")


class Server:
    def __init__(self):
        self.app = web.Application()
        sio = socketio.AsyncServer()
        sio.attach(self.app)

        self.controllerID: str

        @sio.event
        async def connect(sid, environ):
            print("Controller connected with ID {}".format(sid))
            if debug_mode:
                print("Environment : {}".format(environ))
            self.controllerID = sid

        @sio.on('start_camera')
        async def start_camera(sid):
            authenticate_controller(self.controllerID, sid)
            camera_port = config.get_param("camera.port")
            print("Starting camera on port {}...".format(camera_port))
            try:
                camera.start_camera(config.get_param("camera.width"), config.get_param("camera.height"),
                                    config.get_param("camera.fps"), camera_port)
                print("Started camera on port {} !".format(camera_port))
                await sio.emit(event='start_camera', to=self.controllerID)
            except Exception as e:
                print("Unable to start camera for reason : {}".format(e))
                await sio.emit(event='error', data=e, to=self.controllerID)

        @sio.event
        def disconnect(sid):
            print('disconnect ', sid)
