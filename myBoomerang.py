import pip
import sys

try:
	import cv2
except ImportError:
	pip.main(['install', 'opencv-python']) 

videoname  = sys.argv[1]
cap = cv2.VideoCapture(videoname)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video_time = cap.get(cv2.CAP_PROP_FRAME_COUNT) * fps
frame_msec = int (1000 / fps)

fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter(videoname[:-4] + "_boomerang.mp4", 0x7634706d, fps, size)

cap = cv2.VideoCapture(videoname)
print(videoname, "loaded.")
time = 0 
while cap.isOpened():
    while (time < video_time ):
        time = time + frame_msec
        cap.set(cv2.CAP_PROP_POS_MSEC, time)

        ret, frame = cap.read()
       
        out.write(frame)
        
        if (cv2.waitKey(1) >= 0):
            break

    while (video_time > 0):
        video_time = video_time - frame_msec
        cap.set(cv2.CAP_PROP_POS_MSEC, video_time)

        ret, frame = cap.read()
        
        out.write(frame)
        
        if (cv2.waitKey(1) >= 0):
            break
    cap.release()
    out.release()
	
print(videoname[:-4] + "_boomerang.mp4", "created.")
