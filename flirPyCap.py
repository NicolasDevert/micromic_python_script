#!/usr/bin/python

import sys
from flirClass import camera

try:
    flir = camera()
except TypeError:
    print "Error: Aravis found no Camera." 
    print "Check Connections"
    sys.exit(2)
else:
    print flir.device
    flir.make_stream()
    flir.camera.start_acquisition()
    flir.path = "/home/micromet/repo/flirPyCapSd/data/"


flir.run_camera()
