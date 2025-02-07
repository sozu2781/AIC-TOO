import cv2
import numpy as np
from PIL import Image
from morikawa_28m import image_recognition

video_file ="01-03.mp4"
def judge_fromVideo(video_file, frame_interval=6):

    cap =cv2.VideoCapture(video_file)
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
        img=Image.fromarray(frame)
        img=img.resize((1280,720))
        #frame=np.array(img)
        #print(frame.shape)
        
        #秒数計算
        second= (frame_interval/fps)*scan_count
        minute=int(second//60)
        second=int(second%60)
        time =str(minute)+"m "+str(second)+'s'
        
        #img.save('read '+time+'.png')
        #print("save")
        ans= image_recognition(img,time)
        
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