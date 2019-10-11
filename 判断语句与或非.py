
'''
if语句的应用，以及while的循环跳出
'''
while(1):

	my_age = 24		
	my_name = 'Maxwell'

	print("你觉得我的年龄是？")
	guss_age = int(input())
	print("名字呢？")
	guss_name = str(input()) 

	if guss_age==my_age and guss_name==my_name:
		print ("恭喜你,都答对了")
		break
	elif guss_age!=my_age and guss_name!=my_name:
		print("都猜错了，再猜")
	elif guss_age!=my_age:
		print("年龄错了，再猜~\n")
	elif guss_name!=my_name:
		print("名字错了，再猜~\n")