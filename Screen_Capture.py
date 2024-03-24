python
import mss

def capture_sscreen():
	with mss.mss() as sct:
		monitor = sct.monitors[0]
		img = sct.grab(monitor)
		return img