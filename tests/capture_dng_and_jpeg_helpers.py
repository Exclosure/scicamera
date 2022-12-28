#!/usr/bin/python3
# Capture a DNG and a JPEG made from the same raw data.
from picamera2 import Picamera2
from picamera2.helpers import Helpers
from picamera2.testing import mature_after_frames_or_timeout

camera = Picamera2()
camera.start_preview()

preview_config = camera.create_preview_configuration()
capture_config = camera.create_still_configuration(raw={})
camera.configure(preview_config)

camera.start()

mature_after_frames_or_timeout(camera, 2).result()
camera.switch_mode_async(capture_config)
buffers, metadata = camera.capture_buffers_async(["main", "raw"])

Helpers.save(
    camera, Helpers.make_image(buffers[0], capture_config["main"]), metadata, "full.jpg"
)
Helpers.save(camera, buffers[1], metadata, "full.jpeg")
