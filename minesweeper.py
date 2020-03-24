#-*-coding:utf-8*-
import random
a = 9
b = 9
c = 10

#初始化地图
map1=[0 for value in range(1,(a+2)*(b+2)+2)]#存储生成的地图
map2=map1[:]#确定哪些方块是可视的

#随机生成地雷位置
for i in range(0,c):
	d = (random.randint(2,a+1)-1)*(a+2) +random.randint(2,b+1)#随机生成行和列的位置
	print(d)
	map1[d] = -1#-1标记为地雷

#对地图数字进行标号
e = []
for i in range(2,a+2):#遍历每一个有效的格子以确定每个格子之中的数字
	j = 2
	for j in range(2,b+2):
		if map1[(i-1)*(a+2) + j] ==0:#确定第i行j列的数字是不是炸弹，而后检索其周围八格有无地雷，d暂时存储周围炸弹值
			d = 0
			if map1[(i-1)*(a+2) + j + 1] == -1:
				d = d +1
			if map1[(i-1)*(a+2) + j -1 ] == -1:
				d = d +1
			if map1[(i-2)*(a+2) + j ] == -1:
				d = d +1
			if map1[(i-2)*(a+2) + j +1] == -1:
				d = d +1
			if map1[(i-2)*(a+2) + j -1] == -1:
				d = d +1
			if map1[(i)*(a+2) + j ] == -1:
				d = d +1
			if map1[(i)*(a+2)+j-1] == -1:
				d = d +1
			if map1[(i)*(a+2)+j+1] == -1:
				d = d +1
			map1[(i-1)*(a+2)+j] = d
	print(map1[(i-1)*(a+2)+2:i*(a+2)])	

#寻找一个为0的方格作为模拟的第一次点击的方格
i = 2
j = 2
while map1[(i-1)*(a+2) + j]!=0:
	j = j + 1
	if j >= b + 2:#当超过右边界时，换入下一行
		j = 2
		i = i + 1
print(str((i-1)*(a+2) + j))
print(map1[(i-1)*(a+2) + j])
search1=[(i-1)*(a+2) + j]

#加入边框条件限制，对边界元素赋值为-2
for i in range(1,a+3):
	map1[(i-1)*(a+2)+1]=-2
	map1[i*(a+2)]=-2
for i in range(1,b+3):
	map1[i]=-2
	map1[(a+2)*(b+2)+1-i]=-2

#生成一次点击之后的视野（已实现）将有数字的元素存入另一数组（未实现）优化数据结构（未实现）
for i in search1:
	if map1[i+1] == 0 and (i+1) not in search1:
		search1.append(i+1)
	if map1[i-1] == 0 and (i-1) not in search1:
		search1.append(i-1)
	if map1[i-a-2] == 0 and (i-a-2) not in search1:
		search1.append(i-a-2)
	if map1[i+a+2] == 0 and (i+a+2) not in search1:
		search1.append(i+a+2)
	if map1[i-a-3] == 0 and (i-a-3) not in search1:
		search1.append(i-a-3)
	if map1[i-a-1] == 0 and (i-a-1) not in search1:
		search1.append(i-a-1)
	if map1[i+a+1] == 0 and (i+a+1) not in search1:
		search1.append(i+a+1)
	if map1[i+a+3] == 0 and (i+a+3) not in search1:
		search1.append(i+a+3)
	map2[i] = 1
for i in range(2,a+2):
	print(map2[(i-1)*(a+2)+2:i*(a+2)])
