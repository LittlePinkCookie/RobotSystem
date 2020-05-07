import os


def start_camera(vw, vh, fps, port) -> None:
    os.system("raspivid -t 0 -w {} -h {} -hf -ih -fps {} -o - -a 12 | nc -k -l {}".format(vw, vh, fps, port))
