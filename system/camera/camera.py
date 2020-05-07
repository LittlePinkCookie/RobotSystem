import os
import subprocess
from subprocess import Popen
from threading import Thread


def start_camera(vw, vh, fps, port) -> None:
    # Thread. os.system("raspivid -t 0 -w {} -h {} -hf -ih -fps {} -o - -a 12 | nc -k -l {}".format(vw, vh, fps, port))
    p = Popen(['./starter.sh', str(vw), str(vh), str(fps), str(port)])
    # output = subprocess.check_output(('nc', '-k', '-l', str(port)), stdin=p.stdout)
