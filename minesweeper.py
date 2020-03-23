import random
a = 9
b = 9
c = 10
i = 1
map1=[0]
map2=[0]
while i <= (a+2)*(b+2):
	map1.append(0)
	map2.append(0)
	i = i + 1
i = 1

while i <= c:
	d = (random.randint(2,a+1)-1)*(a+2) +random.randint(2,b+1)
	print(d)
	map1[d] = -1
	i = i + 1
i = 2
d = 0
e = []
while i <= a + 1:
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
while map1[(i-1)*(a+2) + j]!=0:
	j = j + 1
	if j >= b + 2:
		j = 2
		i = i + 1
print(str((i-1)*(a+2) + j))
print(map1[(i-1)*(a+2) + j])
search1=[(i-1)*(a+2) + j]
for i in search1:
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
