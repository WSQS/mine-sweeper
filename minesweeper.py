import random
a = 9
b = 9
c = 10
i = 1
map1=[0]#存储生成的地图
map2=[0]#确定哪些方块是可视的
while i <= (a+2)*(b+2):#2到a+1与2到b加1为真正游戏地图，其余区域为避免溢出采用
	map1.append(0)
	map2.append(0)
	i = i + 1
i = 1

while i <= c:#随机生成炸弹位置
	d = (random.randint(2,a+1)-1)*(a+2) +random.randint(2,b+1)
	print(d)
	map1[d] = -1
	i = i + 1
i = 2
d = 0
e = []
while i <= a + 1:#便利每一个格子以确定每个格子之中的数字
	j = 2
	while j <= b + 1:
		if map1[(i-1)*(a+2) + j] ==0:
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
			if map1[(i)*(a+2) + j -1] == -1:
				d = d +1
			if map1[(i)*(a+2) + j +1] == -1:
				d = d +1
			f=(i-1)*(a+2)+j 
			map1[f] = d
		j=j+1
		d = 0
	print(map1[(i-1)*(a+2)+2:i*(a+2)])
	i = i+ 1	
i = 2
j = 2
while map1[(i-1)*(a+2) + j]!=0:#寻找一个为0的方格作为模拟的第一次点击的方格
	j = j + 1
	if j >= b + 2:
		j = 2
		i = i + 1
print(str((i-1)*(a+2) + j))
print(map1[(i-1)*(a+2) + j])
search1=[(i-1)*(a+2) + j]
for i in search1:#生成一次点击之后的视野（未实现）
	if map1[i+1] == 0:
		search1.append(i+1)
	if map1[i-1] == 0:
		search1.append(i-1)
	if map1[i-a-2] == 0:
		search1.append(i-a-2)
	if map1[i+a+2] == 0:
		search1.append(i+a+2)
	if map1[i-a-3] == 0:
		search1.append(i-a-3)
	if map1[i-a-1] == 0:
		search1.append(i-a-1)
	if map1[i+a+1] == 0:
		search1.append(i+a+1)
	if map1[i+a+3] == 0:
		search1.append(i+a+3)
	map2[i] = "x"
print(map2)
