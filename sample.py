import numpy as np
from PIL import Image

im=Image.open("Teacher_1-1_20.png")
ar=np.array(im)
h=len(ar)
w=len(ar[0])
hair=[137,106,55]
#髪の部分について
f=0
for i in range(h):
	cnt=0
	cnt=0
	for j in range(w):
		p=0
		for k in range(3):
			p+=abs(ar[i][j][k]-hair[k])
		if p<=30:
			cnt+=1
		else:
			cnt=0
		if cnt>=10:
			hi=i;hj=j-10
			f=1
			break
	if f==1:
		break
#目の部分について
f=0
for i in range(hi+100,h):
	cnt=0
	cnt=0
	for j in range(hj-100,hj+100):
		if ar[i][j][1]>=ar[i][j][0]*2 and ar[i][j][1]>=ar[i][j][2]:
			cnt+=1
		else:
			cnt=0
		if cnt>=5:
			ei=i;ej=j-10
			f=1
			break
	if f==1:
		break

# print(hi,hj)
# print(ei,ej)
ei+=10

for l in range(hi-5,hi+5):
	for j in range(hj,hj+10):
		ar[l][j]=[0,0,0]

for l in range(ei-5,ei+5):
	for j in range(ej,ej+10):
		ar[l][j]=[0,0,0]

ribon_h1=int((ei-hi)/14*13+ei)
ribon_h2=int((ei-hi)/14*23+ei)

center=hj+10
# for l in range(ribon_h1,ribon_h2):
# 	for j in range(center-5,center+5):
# 		ar[l][j]=[0,0,0]

f=0
ar=ar.astype(np.uint16)
for i in range((ribon_h1+ribon_h2)//2,ribon_h2):
	for j in range(center-50,center+50):
		if sum(ar[i][j])>=600 and sum(ar[i][j+1])<=400:
			ribon=(ar[i][j+5]+ar[i][j+6]+ar[i][j+7]\
				+ar[i][j+8]+ar[i][j+9])//5
			# print(ar[i][j+5],ar[i][j+6],ar[i][j+7]\
			# 	,ar[i][j+8],ar[i][j+9])
			# print(i,j)
			f=1
			break
	if f:
		break
ar=ar.astype(np.uint8)
print(ribon)
if ribon[1]>ribon[0]*2 and ribon[1]>ribon[2]:
	print("OK")
else:
	print("NG")

# print()
# for i in range(-2,3):
# 	for j in range(5,10):
# 		print(ar[381+i][656+j])
# 		ar[381+i][656+j]=[255,255,0]

im=Image.fromarray(ar)
im.save("output.png")