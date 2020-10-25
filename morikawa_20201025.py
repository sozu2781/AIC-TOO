import numpy as np
from PIL import Image
'import cv2'

filename="Teacher_1-2_58.png"#ここにファイルネームを入れる
im=Image.open(filename)
ar=np.array(im)
h=len(ar)
w=len(ar[0])

face=np.zeros((h,w+1))
basyo_h=0
basyo_w=0
hadamax_atai=0


#ジャッジ関数（肌の色）
def judge_hadairo(i,j):
    R=int(ar[i][j][0])
    G=int(ar[i][j][1])
    B=int(ar[i][j][2])
    if R > G and R > B:
        return R > 240 and G > 210 and G <240 and B > 190


def hadakensyutu():
    for i in range(h):
        for j in range(w):
            if judge_hadairo(i,j) == 1:
                ar[i][j]=[0,0,0]
                face[i][j]=1

def hada_suuji():
    for i in range(h):
        for j in range(w):
            if face[i][j] != 0 and face[i][j+1] == 1:
                face[i][j+1]=face[i][j]+1

def hada_yoko():
    global hadamax_atai
    global basyo_h
    global basyo_w
    hadamax_atai=int(np.max(face))
    hadamax_basyo=np.argmax(face)
    basyo_h=int(hadamax_basyo/(w+1))
    basyo_w=hadamax_basyo%(w+1)
    
    print(basyo_h)
    print(basyo_w)

def agotasikame():
    ago=np.zeros((h,w))
    ago_h=[0,0]
    for y in range(hadamax_atai-1-6):
        ago_w=basyo_w-y-3
        ago[basyo_h][ago_w]=1
        
    for j in range(basyo_w):
        for i in range(h-2):
            if ago[i][j] != 0:
                if face[i+1][j]!=0 and face[i+2][j]==0:
                    ago[i+1][j]=ago[i][j]+1
                    ago_h[1]=i                    
                elif face[i+1][j]!=0:
                    ago[i+1][j]=ago[i][j]+1
            elif i>basyo_h and i<ago_h[0]-5:
                ago[i][j]=ago[i-1][j]+1
                ago[i+1][j]=ago[i][j]+1
        ago_h[0]=ago_h[1]

    for i in range(h):
        for j in range(w):
            if ago[i][j] != 0:
                ar[i][j]=[255,0,0]
                             


hadakensyutu()
hada_suuji()
hada_yoko()
agotasikame()


print(hadamax_atai)




im=Image.fromarray(ar)
im.save(filename+'face1.png')