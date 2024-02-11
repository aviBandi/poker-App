from multiprocessing import freeze_support

from ultralytics import YOLO

model = YOLO("yolov8m.pt")

if __name__ == '__main__':
    # freeze_support()
    model.train(data='C:\\Users\\aviba\Downloads\\cardsDataset\data.yaml', epochs=50000, imgsz=640, device=0)
