from lib.akari_yolo_lib.oakd_yolo import OakdYolo
from akari_client import AkariClient
from akari_client.color import Colors
from akari_client.position import Positions
import time #あとで消してもいい
import cv2
import depthai as dai

def main():
    #Ubuntu側には depthai と opencv-python が必要
    # qを押すまでカメラの起動(モデル不要)
    pipeline = dai.Pipeline()

    cam = pipeline.create(dai.node.ColorCamera)
    cam.setPreviewSize(640, 480)

    xout = pipeline.create(dai.node.XLinkOut)
    xout.setStreamName("rgb")

    cam.preview.link(xout.input)

    with dai.Device(pipeline) as device:
        qRgb = device.getOutputQueue("rgb")

        while True:
            frame = qRgb.get().getCvFrame()

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) == ord('q'):
                break

    cv2.destroyAllWindows()


"""     # カメラの起動(モデルが必要)
    oakd_yolo = OakdYolo(
        "json/best.json", 
        "model/best_openvino_2022.1_6shave.blob", # このファイルの中身が分からない(自分でyoloモデルを作るらなきゃ？)
        10
    )
    
    start = time.time()

    while time.time() - start < 5: #5秒実行
        # frameにカメラ画像（NumPy配列），detectionsに検出結果（リスト）が入る
        frame, detections = oakd_yolo.get_frame()

        # 表示
        oakd_yolo.display_frame(
            "OAK-D Camera", # 表示するウィンドウの名前
            frame, # カメラ画像
            detections # 検出結果
        )

        cv2.waitKey(1) #画面更新

    # カメラ終了
    oakd_yolo.close()
    # OpenCVのウィンドウを閉じる
    cv2.destroyAllWindows() """