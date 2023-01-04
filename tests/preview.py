#!/usr/bin/python3

# Normally the QtGlPreview implementation is recommended as it benefits
# from GPU hardware acceleration.

import time

from picamera2 import CameraConfig, Picamera2

camera = Picamera2()
camera.start_preview()

preview_config = CameraConfig.for_preview(camera)
camera.configure(preview_config)

camera.start()
camera.discard_frames(2).result()
camera.stop()
camera.close()
