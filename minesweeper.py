#-*-coding:utf-8*-
import random
a = 9
b = 9
c = 10

#��ʼ����ͼ
map1=[0 for value in range(1,(a+2)*(b+2)+2)]#�洢���ɵĵ�ͼ
#����߿��������ƣ��Ա߽�Ԫ�ظ�ֵΪ-2
for i in range(1,a+3):
	map1[(i-1)*(b+2)+1]=-2
	map1[i*(b+2)]=-2
for i in range(1,b+3):
	map1[i]=-2
	map1[(a+2)*(b+2)+1-i]=-2
map2=map1[:]#ȷ����Щ�����ǿ��ӵ�
map3=map1[:]#�洢��֪������


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

for i in range((a+2)*(b+2)//2,(a+2)*(b+2)+1):
	if map1[i]==0:
		break
print(str(i))
print(map1[i])
search1=[i]
search2=[]

#������Ұ
def search_1():
	flag1 = 0
	for i in search1:
		for k in get_around(i):
			if map1[k] == 0 and k not in search1:
				search1.append(k)
				flag1 = 1
			elif map1[k] != -1 and map1[k] != -2 and k not in search2 and k not in search1:
				search2.append(k)
				map2[k]=2
				flag1 = 1
		map2[i] = 1
	return flag1

#�������ֵķ�����д���
def search_2():
	flag1 = 0
	for i in search2:
		d = 0
		e = []
		f = 0
		for k in get_around(i):
			if map2[k] == 0:
				d=d+1
				e.append(k)
			elif map2[k] == 3:
				f=f+1
		if (d+f) == map1[i]:
			for j in e:
				map2[j]=3
				flag1 = 1
		if f == map1[i]:
			for k in get_around(i):
				if map1[k] != -1 and map1[k] != -2 and k not in search2 and k not in search1:
					search1.append(k)
					flag1 = 1
	return flag1
#��һ�׶ε�����
def part1():
	flag = 1#�ж�һ��ѭ��֮�����ޱ仯
	while flag:
		flag = search_1() or search_2()
		for i in range(2,a+2):
			print(map2[(i-1)*(b+2)+2:i*(b+2)])
		print("\n")
part1()
for i in range(2,a+2):
	print(map1[(i-1)*(b+2)+2:i*(b+2)])
