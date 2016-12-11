def print_one (*chanshu):
		chanshu1,chanshu2=chanshu
		print("chanshu1 is %r,chanshu2 is %s" % (chanshu1,chanshu2))
def print_two (cs1,cs2):
    print ("cs1 is %s cs2 is %s" % (cs1,cs2))
def print_three (cs3):
    print ("cs3 is ",cs3)
def print_x ():
    print ("这个函数不接受参数")
print_one ("ab","cd")
print_two ("ab","cd")
print_three("abcd")
print_x()


#注意三个问题：
#1.Python对缩进问题要求的真是非常严格，因为它没有{}代码标识块，notepad++编辑器中，函数的定义超过行就要按两个tab键
#2.自定义函数，使用函数时，接受的参数要用引号
