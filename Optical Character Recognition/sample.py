import subprocess
import time
import subprocess
from PIL import Image
import cv2
from dpi import set300dpi
import correct_skew
from correct_skew import rotate
from correct_skew import binary
import thresholding
from thresholding import denoise
import segmentation
from segmentation import segment

		
print('Button Pressed')
		
print("Get ready with your webcam")
		
print('Taking snap in next 10seconds')
		
time.sleep(1)	
		
print("Taking snap")
#camera module
#take img from camera module
img= cv2.imread("/home/pi/cam.jpg")

#set image to 300dpi
#image= set300dpi(img) 

#binarisation and rotation
print("Binarising image")
print("Fixing skew angles")
a=binary(img)
rotated= rotate(a)


#threshold and denoise

print("Thresholding and denoising image")
denoised= denoise(rotated)

	#segmentation of image
segment(denoised)
		
print("Performing OCR")

		
subprocess.call(['tesseract', '/home/pi/Desktop/denoised.jpg', 'speech2'])
		
print("The detected text is")
		
subprocess.call(['cat', 'speech2.txt'])
                
print("Speaking text")
		
subprocess.call(['festival', '--tts', 'speech2.txt'])        


