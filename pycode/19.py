def choosenum(*num):
		num1,num2=num
		print ("你有%d选择" % num1)
		print ("你有%d另一种选择" % num2)


print ("python中使用自定义函数的时候可以在接受的参数中写入计算式")

choosenum(100*2,20/9**3+23)
