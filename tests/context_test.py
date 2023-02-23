from scicamera import Camera, CameraConfig


def test_context_manager():
    print("With context...")
    with Camera() as camera:
        config = CameraConfig.for_preview(camera)
        camera.configure(config)
        camera.start()
        metadata = camera.capture_metadata().result()
        assert isinstance(metadata, dict)
        print(metadata)

    print("Without context...")
    camera = Camera()
    config = CameraConfig.for_preview(camera)
    camera.configure(config)
    camera.start()
    metadata = camera.capture_metadata().result()
    print(metadata)
    camera.stop_preview()
    camera.close()
