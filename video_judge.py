import cv2
import numpy as np
from PIL import Image


video_file ="01-01.mp4"
def judge_fromVideo(video_file, frame_interval=30):

    cap =cv2.VideoCapture(video_file)
    print(cap.isOpened())
    fps =cap.get(cv2.CAP_PROP_FPS)
    #print(round(fps))
    
    scan_count =0
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_interval*scan_count)
        ret, frame_bgr = cap.read()
        if frame_bgr==None:
            break
        frame =frame_bgr[:,:,[2,1,0]]
        
        #ここにリボンの色正誤判定を入れる
        ans=
        
        
        error_list =[]
        if ans==False:
            second= (frame_interval/fps)*scan_count
            minute=second//60
            second=second%60
            error_list.append(str(minute)+":"+str(second))
        
        scan_count +=1
        
    print(error_list)

"""
im=Image.fromarray(frame)
im.save('test.png')

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
print(cap.get(cv2.CAP_PROP_POS_MSEC))
"""