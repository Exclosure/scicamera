#!/usr/bin/python3

import time

from picamera2 import CameraConfiguration, Picamera2

camera1 = Picamera2(0)
camera1.configure(CameraConfiguration.create_preview_configuration(camera1))
camera1.start_preview()

camera2 = Picamera2(1)
camera2.configure(CameraConfiguration.create_preview_configuration(camera2))
camera2.start_preview()

camera1.start()
camera2.start()
time.sleep(2)
camera1.stop_preview()
camera2.stop_preview()

time.sleep(2)

camera1.start_preview()
camera2.start_preview()

time.sleep(2)
camera1.close()
camera2.close()
