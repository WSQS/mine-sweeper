#-*-coding:utf-8*-
import random
a = 9
b = 9
c = 10

#��ʼ����ͼ
map1=[0 for value in range(1,(a+2)*(b+2)+2)]#�洢���ɵĵ�ͼ
map2=map1[:]#ȷ����Щ�����ǿ��ӵ�

#������ɵ���λ��
for i in range(0,c):
	d = (random.randint(2,a+1)-1)*(a+2) +random.randint(2,b+1)#��������к��е�λ��
	print(d)
	map1[d] = -1#-1���Ϊ����

#��ȡi������Χ��������ĺ���
def get_around(i):
	around=[]
	around.append(i+1)
	around.append(i-1)
	around.append(i+a+2)
	around.append(i+a+3)
	around.append(i+a+1)
	around.append(i-a-2)
	around.append(i-a-1)
	around.append(i-a-3)
	return around

#�Ե�ͼ���ֽ��б��
for i in range(2,a+2):#����ÿһ����Ч�ĸ�����ȷ��ÿ������֮�е�����
	j = 2
	for j in range(2,b+2):
		if map1[(i-1)*(b+2) + j] ==0:#ȷ����i��j�е������ǲ���ը���������������Χ�˸����޵��ף�d��ʱ�洢��Χը��ֵ
			d = 0
			for k in get_around((i-1)*(b+2)+j):
				if map1[k] == -1:
					d = d+1
			map1[(i-1)*(b+2)+j] = d
	print(map1[(i-1)*(b+2)+2:i*(b+2)])	

#Ѱ��һ��Ϊ0�ķ�����Ϊģ��ĵ�һ�ε���ķ���
i = 2
j = 2
while map1[(i-1)*(b+2) + j]!=0:
	j = j + 1
	if j >= b + 2:#�������ұ߽�ʱ��������һ��
		j = 2
		i = i + 1
print(str((i-1)*(b+2) + j))
print(map1[(i-1)*(b+2) + j])
search1=[(i-1)*(b+2) + j]

#����߿��������ƣ��Ա߽�Ԫ�ظ�ֵΪ-2
for i in range(1,a+3):
	map1[(i-1)*(b+2)+1]=-2
	map1[i*(b+2)]=-2
for i in range(1,b+3):
	map1[i]=-2
	map1[(a+2)*(b+2)+1-i]=-2

#����һ�ε��֮�����Ұ����ʵ�֣��������ֵ�Ԫ�ش�����һ���飨δʵ�֣��Ż����ݽṹ��δʵ�֣�
for i in search1:
	for k in get_around(i):
		if map1[k] == 0 and k not in search1:
			search1.append(k)
	map2[i] = 1
for i in range(2,a+2):
	print(map2[(i-1)*(b+2)+2:i*(b+2)])
