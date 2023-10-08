# yolov7
customize yolov7

# guides

- Download trained weights

        mkdir trained
        cd trained
        wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
        cd ..

- Detection: `python detect.py --weights trained/yolov7.pt --conf 0.25 --img-size 640 --source inference/images/horses.jpg`

# references

[Official YOLO v7 Object Detection COMPLETE Tutorial for Google Colab](https://www.youtube.com/watch?v=_CkXDjmT8dc)

[ How to Train YOLOv7 On a Custom Dataset ](https://www.youtube.com/watch?v=5nsmXLyDaU4)

[yolov7-github](https://github.com/WongKinYiu/yolov7)