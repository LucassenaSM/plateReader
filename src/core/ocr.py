import cv2 
import pytesseract 
import re 
import os 
from src.config.constants import TESSERACT_CMD
 
tesseract_path = os.getenv('TESSERACT_CMD', TESSERACT_CMD) 
if os.path.exists(tesseract_path): 
    pytesseract.pytesseract.tesseract_cmd = tesseract_path 
else: 
    pytesseract.pytesseract.tesseract_cmd = 'tesseract'
 
class PlateOCR: 
    def __init__(self): 
        self.pattern = re.compile(r'([A-Z]{3}\d{4}|[A-Z]{3}\d[A-Z]\d{2})')
 
    def preprocess(self, image): 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
        blur = cv2.GaussianBlur(thresh, (5, 5), 1) 
        return blur
 
    def read_plate(self, image): 
        processed_img = self.preprocess(image) 
        try: 
            text = pytesseract.image_to_string(processed_img, config='--psm 6') 
        except Exception: 
            return None
 
        text = text.upper().replace('-', '').replace(' ', '').strip() 
        match = self.pattern.search(text) 
        if match: 
            return match.group() 
        return None
