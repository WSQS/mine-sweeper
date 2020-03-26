#-*-coding:utf-8*-
import random
a = 9
b = 9
c = 10

#初始化地图
map1=[0 for value in range(1,(a+2)*(b+2)+2)]#存储生成的地图
#加入边框条件限制，对边界元素赋值为-2
for i in range(1,a+3):
	map1[(i-1)*(b+2)+1]=-2
	map1[i*(b+2)]=-2
for i in range(1,b+3):
	map1[i]=-2
	map1[(a+2)*(b+2)+1-i]=-2
map2=map1[:]#确定哪些方块是可视的
map3=map1[:]#存储已知的数字


#随机生成地雷位置
for i in range(0,c):
	d = (random.randint(2,a+1)-1)*(a+2) +random.randint(2,b+1)#随机生成行和列的位置
	print(d)
	map1[d] = -1#-1标记为地雷

#获取i序数周围方格坐标的函数
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

#对地图数字进行标号
for i in range(2,a+2):#遍历每一个有效的格子以确定每个格子之中的数字
	j = 2
	for j in range(2,b+2):
		if map1[(i-1)*(b+2) + j] ==0:#确定第i行j列的数字是不是炸弹，而后检索其周围八格有无地雷，d暂时存储周围炸弹值
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

#生成视野
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

#对有数字的方块进行处理
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
#第一阶段的运行
def part1():
	flag = 1#判定一个循环之中有无变化
	while flag:
		flag = search_1() or search_2()
		for i in range(2,a+2):
			print(map2[(i-1)*(b+2)+2:i*(b+2)])
		print("\n")
part1()
for i in range(2,a+2):
	print(map1[(i-1)*(b+2)+2:i*(b+2)])
