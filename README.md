# yolov7
customize yolov7

# guides

install `simple_image_download`: `pip install simple-image-download`

install annotation tools `pip install labelImg`

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

# references

[Official YOLO v7 Object Detection COMPLETE Tutorial for Google Colab](https://www.youtube.com/watch?v=_CkXDjmT8dc)

[ How to Train YOLOv7 On a Custom Dataset ](https://www.youtube.com/watch?v=5nsmXLyDaU4)

[yolov7-github](https://github.com/WongKinYiu/yolov7)