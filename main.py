import pyautogui
import time
from pytesseract import pytesseract
from PIL import Image
import keyboard

while 1:
    if keyboard.is_pressed('v'):
        time.sleep(0.4)
        im = pyautogui.screenshot(region=(460,600, 985, 200))
        im.save(r'ss.png')
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = r'ss.png'
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        text = text.replace("\n", " ")
        text = text.replace("change display format", "")
        text = text.replace("|", "I")
        text = text.replace("@", "")
        text = text.replace("II", "I")
        text = text.replace("[", "")
        text = text.replace("{", "")
        pyautogui.write(text[:-1], interval=0.09)
        time.sleep(0.6)