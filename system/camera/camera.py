from subprocess import Popen


def start_camera(vw, vh, fps, port) -> None:
    Popen(['system/camera/starter.sh', str(vw), str(vh), str(fps), str(port)])
