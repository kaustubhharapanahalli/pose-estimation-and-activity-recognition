from imutils import paths
import numpy as np
import cv2
import sys
import os

def Humans(): 
	args = {'videotoframe': 'videotoframe'}

	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	try:
		if not os.path.exists('humandetected'):
			os.makedirs('humandetected')
	except OSError:
		print('Error: Creating directory of humandetected')

	iterator = 0
	for imagePath in paths.list_images(args["videotoframe"]):
		print(imagePath)
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
		
		print((type(rects), type(weights)))
		if len(rects) != 0 and len(weights) !=0 :
			
			print ("human")
			cv2.imwrite( 'humandetected/' + str(iterator) + '.jpg',image) #(orig)
			iterator += 1
			for (x, y, w, h) in rects:
				cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
Humans()
