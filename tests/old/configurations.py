#!/usr/bin/python3

from scicamera import Camera
from scicamera.testing import requires_controls

camera = Camera()

requires_controls(camera, ("ExposureTime", "FrameDurationLimits"))

# We're going to set up some configuration structures, apply each one in
# turn and see if it gave us the configuration we expected.

camera.preview_configuration.size = (800, 600)
camera.preview_configuration.format = "RGB888"
camera.preview_configuration.controls.ExposureTime = 10000

camera.video_configuration.main.size = (800, 480)
camera.video_configuration.main.format = "YUV420"
camera.video_configuration.controls.set_frame_rate(25.0)

camera.still_configuration.size = (1024, 768)
camera.still_configuration.enable_lores()
camera.still_configuration.lores.format = "YUV420"
camera.still_configuration.enable_raw()
half_res = tuple([v // 2 for v in camera.sensor_resolution])
camera.still_configuration.raw.size = half_res

camera.configure("preview")
if camera.controls.ExposureTime != 10000:
    raise RuntimeError("exposure value was not set")
config = camera.camera_configuration()
if config.main.size != (800, 600):
    raise RuntimeError("preview resolution incorrect")

camera.configure("video")
frame_rate = camera.controls.get_frame_rate()
if frame_rate < 24.99 or frame_rate > 25.01:
    raise RuntimeError("framerate was not set")
config = camera.camera_configuration()
if config.size != (800, 480):
    raise RuntimeError("video resolution incorrect")
if config.format != "YUV420":
    raise RuntimeError("video format incorrect")

camera.configure("still")
config = camera.camera_configuration()
if config.raw.size != half_res:
    raise RuntimeError("still raw size incorrect")

camera.close()
