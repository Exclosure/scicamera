from typing import Type

import pytest

from scicamera import Camera, CameraConfig, FakeCamera
from scicamera.configuration import CameraConfig
from scicamera.testing import mature_after_frames_or_timeout, requires_camera_model


@pytest.mark.parametrize("CameraClass", [Camera, FakeCamera])
def test_capture_buffers_and_metadata(CameraClass: Type[Camera]):
    with CameraClass() as camera:
        requires_camera_model(camera, "imx", allow_fake=False)

        camera.start_runloop()

        preview_config = CameraConfig.for_preview(camera)
        capture_config = CameraConfig.for_still(camera, raw={})
        camera.configure(preview_config)

        camera.start()
        mature_after_frames_or_timeout(camera)
        camera.switch_mode(capture_config).result(timeout=5.0)
        buffers, metadata = camera.capture_buffers_and_metadata(["main", "raw"]).result(
            timeout=5.0
        )

        camera.stop()

    assert isinstance(buffers, list)
    assert len(buffers) == 2
    assert isinstance(metadata, dict)
