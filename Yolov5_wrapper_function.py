python
import torch

def detect_ui_elements(img):
	model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/custom/model.pt')
	results = model(img)
	return results.pandas().xyxy[0].to_dict(orient='records')