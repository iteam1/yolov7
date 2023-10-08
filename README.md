# yolov7
customize yolov7

# guides

install `simple_image_download`: `pip install simple-image-download`

install annotation tools `pip install labelImg`

install `tensorboard`: `pip install tensorboard`

install `onnx`: `pip install onnx`

install `seaborn`: `pip install seaborn`

install `onnxruntime`: `pip install onnxruntime`

install `onnx-simplifier`: `pip install onnx-simplifier>=0.3.6`

- Download trained weights

        mkdir trained
        cd trained
        wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
        cd ..

- QuickStart: `python detect.py --weights trained/yolov7.pt --conf 0.25 --img-size 640 --source inference/images/horses.jpg`

- Train (*Note: training output path runs/train/training*):

        python train.py --workers 1 --device 0 --batch-size 8 --epochs 500 --img 640 640 \
        --data assets/my_coco.yaml --hyp data/hyp.scratch.custom.yaml --cfg assets/my_yolov7.yaml \
         --name training --weights trained/yolov7.pt

- View tensorboard `tensorboard --logdir runs/train/training --host 0.0.0.0 --port 8000`

- Detect custom dataset: `python detect.py --weights runs/train/training/weights/best.pt --conf 0.25 --img-size 640 --source dataset/test/A08Rx.jpg`

- Export ONNX for ONNX inference

        python export.py --weights runs/train/training/weights/best.pt \
        --grid --end2end --simplify \
        --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 \
        --img-size 640 640 --max-wh 640

# references

[Convert and Optimize YOLOv7 with OpenVINO™](https://docs.openvino.ai/2023.1/notebooks/226-yolov7-optimization-with-output.html)

[ONNX-YOLOv7-Object-Detection](https://github.com/ibaiGorordo/ONNX-YOLOv7-Object-Detection/tree/main)

[netron app](https://netron.app/)

[netron](https://github.com/lutzroeder/netron)

[Official YOLO v7 Object Detection COMPLETE Tutorial for Google Colab](https://www.youtube.com/watch?v=_CkXDjmT8dc)

[ How to Train YOLOv7 On a Custom Dataset ](https://www.youtube.com/watch?v=5nsmXLyDaU4)

[yolov7-github](https://github.com/WongKinYiu/yolov7)