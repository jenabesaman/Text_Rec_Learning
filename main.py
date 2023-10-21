import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread("Untitled.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow(winname="rgb",mat=rgb)
# cv2.waitKey()
# cv2.destroyAllWindows()

# config_tesseract= "--tessdata-dir tessdata --psm 6"
# text=pytesseract.image_to_string(image=rgb,lang="fas",config=config_tesseract)
text=pytesseract.image_to_string(image=rgb,lang="fas")
print(text)