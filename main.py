import cv2
import depthai as dai
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Image
import threading

def main():
    #Ubuntu側には depthai と opencv-python が必要
    # qを押すまでカメラの起動(モデル不要)

    # OAK-Dのパイプライン作成
    pipeline = dai.Pipeline()

    # ソースとアウトプットの設定
    cam_rgb = pipeline.createColorCamera()

    # preview size640x480に指定
    cam_rgb.setPreviewSize(640, 480)
    cam_rgb.setInterleaved(False)

    # ストリーミング名設定
    xout_rgb = pipeline.createXLinkOut()
    xout_rgb.setStreamName("rgb")
    cam_rgb.preview.link(xout_rgb.input)

    display_handle=display(None, display_id=True)

    with dai.Device(pipeline) as device:

        while True:
            video = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
            frame = video.get().getCvFrame()


            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        pipeline.stop()


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

if __name__ == "__main__":
    main()