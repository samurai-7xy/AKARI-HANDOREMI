import depthai as dai

class Camera:

    def __init__(self):

        self.pipeline = dai.Pipeline()

        self.cam_rgb = self.pipeline.createColorCamera()
        self.cam_rgb.setPreviewSize(640, 480)
        self.cam_rgb.setInterleaved(False)

        self.xout_rgb = self.pipeline.createXLinkOut()
        self.xout_rgb.setStreamName("rgb")

        self.cam_rgb.preview.link(self.xout_rgb.input)

        self.device = dai.Device(self.pipeline)

        self.video = self.device.getOutputQueue(
            name="rgb",
            maxSize=4,
            blocking=False
        )

    def get_frame(self):
        return self.video.get().getCvFrame()

    def close(self):
        self.device.close()