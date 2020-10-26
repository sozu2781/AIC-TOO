import numpy as np
from PIL import Image
'import cv2'

filename="Teacher_2-2_28.png"#ここにファイルネームを入れる
im=Image.open(filename)
ar=np.array(im)
h=len(ar)
w=len(ar[0])

face=np.zeros((h,w+1))
basyo_h=0
basyo_w=0
basyo_w_left=0
hadamax_atai=0
agomax_basyo_h=0
agomax_basyo_w=0
green_rate=0

ago_ok=0


#ジャッジ関数（肌の色）
def judge_hadairo(i,j):
    R=int(ar[i][j][0])
    G=int(ar[i][j][1])
    B=int(ar[i][j][2])
    if R > G and R > B:
        return R > 240 and G > 210 and G <245 and B > 190


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
    global basyo_w_left
    
    hadamax_atai=int(np.max(face))
    hadamax_basyo=np.argmax(face)
    basyo_h=int(hadamax_basyo/(w+1))
    basyo_w=hadamax_basyo%(w+1)
    
    while hadamax_atai>200:
        print("aaa")
        for j in range(hadamax_atai):
            kesu_w=basyo_w-j
            face[basyo_h][kesu_w]=1
        print(hadamax_atai)
        hadamax_atai=int(np.max(face))
        hadamax_basyo=np.argmax(face)
        basyo_h=int(hadamax_basyo/(w+1))
        basyo_w=hadamax_basyo%(w+1)
    
    basyo_w_left=basyo_w-hadamax_atai+1
    
    print("aa")
    print(basyo_h,basyo_w)
    print(hadamax_atai)

def agotasikame():
    global ago_ok
    global agomax_basyo_h
    global agomax_basyo_w
    ago=np.zeros((h,w))
    ago_h=[0,0]
    ago_maxatai=np.zeros(w)
    for y in range(hadamax_atai-1):
        ago_w=basyo_w-y
        ago[basyo_h][ago_w]=1
        
    for j in range(basyo_w):
        for i in range(h-2):
            if ago[i][j] != 0:
                if face[i+1][j]!=0 and face[i+2][j]==0:
                    ago[i+1][j]=ago[i][j]+1
                    ago_h[1]=i
                    ago_maxatai[j]=i
                    face[i+1][j]=1
                elif face[i+1][j]!=0:
                    ago[i+1][j]=ago[i][j]+1
                    face[i+1][j]=1
            elif i>basyo_h and i<ago_h[0]-5:
                ago[i][j]=ago[i-1][j]+1
                ago[i+1][j]=ago[i][j]+1
        ago_h[0]=ago_h[1]
    
    agomax_basyo=np.argmax(ago)
    agomax_basyo_h=int(agomax_basyo/w)
    agomax_basyo_w=int(agomax_basyo%w)

    
   
    p1=int((basyo_w_left*2+agomax_basyo_w)/3)
    p2=int((basyo_w_left+agomax_basyo_w*2)/3)
    p3=int((basyo_w+agomax_basyo_w*2)/3)
    p4=int((basyo_w*2+agomax_basyo_w)/3)
    p1_h=int(ago_maxatai[p1])
    p2_h=int(ago_maxatai[p2])
    p3_h=int(ago_maxatai[p3])
    p4_h=int(ago_maxatai[p4])
    
    if (agomax_basyo_h-basyo_h)/(agomax_basyo_w-basyo_w_left)+0.1 > (agomax_basyo_h-p1_h)/(agomax_basyo_w-p1) and (agomax_basyo_h-p1_h)/(agomax_basyo_w-p1)+0.1 > (agomax_basyo_h-p2_h)/(agomax_basyo_w-p2) and (agomax_basyo_h-basyo_h)/(basyo_w-agomax_basyo_w)+0.1 > (agomax_basyo_h-p4_h)/(p4-agomax_basyo_w) and (agomax_basyo_h-p4_h)/(p4-agomax_basyo_w)+0.1 > (agomax_basyo_h-p3_h)/(p3-agomax_basyo_w):
        print("good")
        ago_ok=1
    else:
        print("a")
        for j in range(hadamax_atai):
            kesu_w=basyo_w-j
            face[basyo_h][kesu_w]=1

    if ago_ok==1:
        for i in range(h):
            for j in range(w):
                if ago[i][j] != 0:
                    ar[i][j]=[0,255,0]
    else:
        for i in range(h):
            for j in range(w):
                if ago[i][j] != 0:
                    ar[i][j]=[255,0,0]
    
    
    
    
    ar[agomax_basyo_h][agomax_basyo_w]=[0,0,255]
    ar[basyo_h][basyo_w_left]=[0,0,255]
    ar[basyo_h][basyo_w]=[0,0,255]
    
    ar[p1_h][p1]=[0,0,255]
    ar[p2_h][p2]=[0,0,255]
    ar[p3_h][p3]=[0,0,255]
    ar[p4_h][p4]=[0,0,255]
    '''print(p1_h,p1)'''
                             

def ribbon_kakomu():
    global green_rate
    s_h0=agomax_basyo_h+int(hadamax_atai/3)
    s_h1=agomax_basyo_h+int(hadamax_atai)*2
    s_h1=min(s_h1,h-1)
    s_w0=agomax_basyo_w-int(hadamax_atai)
    s_w1=agomax_basyo_w+int(hadamax_atai)
    s_w1=min(s_w1,w-1)
    
    s_h=s_h0
    s_w=s_w0
    count_green=0
    count_all=1
    while s_w<s_w1:
        while s_h<s_h1:
            if ar[s_h][s_w][0] > 10 or face[s_h][s_w] != 0:
                ar[s_h][s_w]=[100,0,0]
            else:
                count_all=count_all+1
                if ar[s_h][s_w][1]>100 and ar[s_h][s_w][1]<160 and ar[s_h][s_w][2]>40 and ar[s_h][s_w][2]<80:
                    count_green=count_green+1
            s_h=s_h+1
        s_w=s_w+1
        s_h=s_h0
    
    green_rate=count_green/count_all
    print(green_rate)


hadakensyutu()
hada_suuji()

while ago_ok==0:
    hada_yoko()
    agotasikame()
    if hadamax_atai < 80:
        print("No face")
        for j in range(w-1):
            ar[0][j]=[0,0,0]
        break
    

if ago_ok==1:
    ribbon_kakomu()
    if green_rate>0.7:
        print("色：正解")
        for j in range(w-1):
            ar[0][j]=[0,255,0]
    else:
        print("色：間違い")
        for j in range(w-1):
            ar[0][j]=[255,0,0]


'''print(hadamax_atai)
print(ago_ok)'''



im=Image.fromarray(ar)
im.save(filename+'ans1.png')