import cv2
import pytesseract


cam = cv2.Capture(2)
ret, image = cam.read()
cv2.imshow('Imagetest',image)
cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()

text = pytesseract.image_to_string(image)
            
cv2.imshow("IDENTITY CARD", image)