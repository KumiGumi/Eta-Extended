python
import pytesseract

def extract_text(img):
	text = pytesseract.image_to_string(img)
	return text
    
#Needs to be preprocessed for better ocr accuracy later