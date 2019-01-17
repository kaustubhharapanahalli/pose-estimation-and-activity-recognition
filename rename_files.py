import os

# path = "D:\\final_year_project_code\\abc22"
path = "D:\\final_year_project_code\\handclapping_pose_estimation2"

files = os.listdir(path)
i = 1452
j = 1
k = 1

for filename in files:
	if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".NEF"):
		os.rename(os.path.join(path, filename), os.path.join(path, "image" + str(i)+'.jpg'))
		print("Renaming " + filename)
		i = i+1
	elif filename.endswith("mp4") or filename.endswith(".MP4"):
		os.rename(os.path.join(path, filename), os.path.join(path, "Varchasva" + str(j)+'.mp4'))
		print("Renaming " + filename)
		j = j+1
	elif filename.endswith(".MOV"):
		os.rename(os.path.join(path, filename), os.path.join(path, "Varchasva" + str(k)+'.MOV'))
		print("Renaming " + filename)
		k = k+1
