import numpy as np
from PIL import Image

filename="Teacher_1-1_22.png"#ここにファイルネームを入れる
im=Image.open(filename)
ar=np.array(im)
h=len(ar)
w=len(ar[0])

#以下はジャッジ関数
def judge_green(i,j):
	R=int(ar[i][j][0])
	G=int(ar[i][j][1])
	B=int(ar[i][j][2])
	return G>=R*2 and G>=B

def Hair_top():
	hair=[137,106,55]
	hi=hj=-1
	f=0
	for i in range(h):
		cnt=0
		for j in range(w):
			p=0
			for k in range(3):
				p+=abs(ar[i][j][k]-hair[k])
			if p<=40:
				cnt+=1
			else:
				cnt=0
			if cnt>=10:
				hi=i;hj=j-5
				f=1
				break
		if f==1:
			break
	return (hi,hj)

def Hair_LeftRight():
	ht=Hair_top()
	hair=[137,106,55]
	hl=-1
	f=0
	for j in range(ht[1]-150,ht[1]):
		cnt=0
		for i in range(ht[0],h):
			p=0
			for k in range(3):
				p+=abs(ar[i][j][k]-hair[k])
			if p<=40:
				cnt+=1
			else:
				cnt=0
			if cnt>=60:
				hl=j-5
				f=1
				break
		if f==1:
			break
	hr=-1
	f=0
	for j in range(ht[1]+150,ht[1],-1):
		cnt=0
		for i in range(ht[0],h):
			p=0
			for k in range(3):
				p+=abs(ar[i][j][k]-hair[k])
			if p<=40:
				cnt+=1
			else:
				cnt=0
			if cnt>=60:
				hr=j-5
				f=1
				break
		if f==1:
			break
	return (hl,hr)	

def Left_Eye():
	ht=Hair_top()
	f=0
	ei=ej=-1;
	for i in range(ht[0]+70,ht[0]+200):
		cnt=0
		for j in range(ht[1]-150,ht[1]-50):
			if judge_green(i,j):
				cnt+=1
			else:
				cnt=0
			if cnt>=5:
				ei=i+10;ej=j
				f=1
				break
		if f==1:
			break
	if f==0:
		for i in range(ht[0]+70,ht[0]+200):
			cnt=0
			for j in range(ht[1]-50,ht[1]):
				if judge_green(i,j):
					cnt+=1
				else:
					cnt=0
				if cnt>=5:
					ei=i+10;ej=j
					f=1
					break
			if f==1:
				break
	if f==0:
		for i in range(ht[0]+70,ht[0]+200):
			cnt=0
			for j in range(ht[1],ht[1]+50):
				if judge_green(i,j):
					cnt+=1
				else:
					cnt=0
				if cnt>=5:
					ei=i+10;ej=j
					f=1
					break
			if f==1:
				break
	return (ei,ej)

def Right_Eye():
	ht=Hair_top()
	f=0
	ei=ej=-1;
	for i in range(ht[0]+70,ht[0]+200):
		cnt=0
		for j in range(ht[1]+150,ht[1]+50,-1):
			if judge_green(i,j):
				cnt+=1
			else:
				cnt=0
			if cnt>=5:
				ei=i+10;ej=j
				f=1
				break
		if f==1:
			break
	if f==0:
		for i in range(ht[0]+70,ht[0]+200):
			cnt=0
			for j in range(ht[1]+50,ht[1],-1):
				if judge_green(i,j):
					cnt+=1
				else:
					cnt=0
				if cnt>=5:
					ei=i+10;ej=j
					f=1
					break
			if f==1:
				break
	if f==0:
		for i in range(ht[0]+70,ht[0]+200):
			cnt=0
			for j in range(ht[1],ht[1]-50,-1):
				if judge_green(i,j):
					cnt+=1
				else:
					cnt=0
				if cnt>=5:
					ei=i+10;ej=j
					f=1
					break
			if f==1:
				break
	return (ei,ej)

def Mouse():
	mouse=[203,102,113]
	ht=Hair_top()
	f=0
	mi=mj=-1;
	for i in range(ht[0]+100,ht[0]+250):
		cnt=0
		for j in range(ht[1]-100,ht[1]+100):
			p=0
			for k in range(3):
				p+=abs(ar[i][j][k]-mouse[k])
			if p<=40:
				cnt+=1
			else:
				cnt=0
			if cnt>=5:
				mi=i+5;mj=j-5
				f=1
				break
		if f==1:
			break
	return (mi,mj)	

def paint(x,y):
	for i in range(-2,3):
		for j in range(-2,3):
			ar[x+i][y+j]=[255,255,0]

a=Hair_top()
b=Hair_LeftRight()
c=Left_Eye()
d=Right_Eye()
e=Mouse()
#hair_LEftRightは(x_Left,x_Right)
#それ以外は(x,y)が返り値である
#該当するものがない場合-1を返す

print(a,b,c,d,e)

def all_paint():
	ht=Hair_top()
	if a[0]!=-1 and a[1]!=-1:
		paint(a[0],a[1])
		if c[0]!=-1 and c[1]!=-1:
			paint(c[0],c[1])
		if d[0]!=-1 and d[1]!=-1:
			paint(d[0],d[1])
		if e[0]!=-1 and e[1]!=-1:
			paint(e[0],e[1])
		if b[0]!=-1 and b[1]!=-1:
			for i in range(ht[0],ht[0]+100):
				paint(i,b[0])
				paint(i,b[1])
	else:
		print("Nothing")

	im=Image.fromarray(ar)
	im.save(filename+'out.png')

all_paint()