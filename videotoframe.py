import cv2
import os
import numpy as np
from PIL import Image
import pose_detector

print(cv2.__version__)
def videoframe():  
	global count
	count = 1
	for videos in os.listdir("videoin"):
		print(videos)
		# print(video)
		vidcap = cv2.VideoCapture("videoin/" + videos)

		try:
			if not os.path.exists('videotoframe'):
				os.makedirs('videotoframe')
		except OSError:
			print('Error: Creating directory of videotoframe')

		success = True
		while success:
			success,image = vidcap.read()

			name = './videotoframe/image' + str(count) + '.jpg'

			print('creating... ' + name)
			if count%8 == 0:
				cv2.imwrite(name ,image) #(orig)

				print('Read a new frame: ', success)

				posedetector = pose_detector.PoseDetector("posenet", "models/coco_posenet.npz", device=-1)
				person_pose_array, _ = posedetector(image)
				res_img = cv2.addWeighted(image, 0.6, pose_detector.draw_person_pose(image, person_pose_array), 0.4, 0)
				cv2.imwrite("pose_estimated/result"+str(count)+".jpg", res_img)
				

			 # save frame as JPEG file
			count += 1
			str(count)
	vidcap.release()
	cv2.destroyAllWindows()

	# vidcap.destroyAllWindows()
	print(count)

videoframe()



