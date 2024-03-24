python
from yolov5 import train

def train_ui_detection_model(data_yaml, epochs=100, batch_size=16):
	train.run(data=data_yaml, epochs=epochs, batch_size=batch_size)