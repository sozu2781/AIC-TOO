import cv2
import numpy as np
from PIL import Image
from morikawa_20201028 import image_recognition

video_file ="01-01_w.mp4"
def judge_fromVideo(video_file, frame_interval=30):

    cap =cv2.VideoCapture(video_file)
    print(cap.isOpened())
    fps =cap.get(cv2.CAP_PROP_FPS)
    #print(round(fps))
    
    scan_count =0
    error_list =[]
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_interval*scan_count)
        ret, frame_bgr = cap.read()
        if ret==False:
            break
        frame =frame_bgr[:,:,[2,1,0]]
        
        #秒数計算
        second= (frame_interval/fps)*scan_count
        minute=int(second//60)
        second=int(second%60)
        time =str(minute)+"m "+str(second)+'s'
        
        ans= image_recognition(frame,time)
        
        if ans==False:
            error_list.append(time)
        
        scan_count +=1
        
    print(error_list)
judge_fromVideo(video_file)

"""
im=Image.fromarray(frame)
im.save('test.png')

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
print(cap.get(cv2.CAP_PROP_POS_MSEC))
"""