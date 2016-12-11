#让python脚本和其它参数运行的一个最好的例子就是：参数中有带路径的文件

from sys import argv

script,filename=argv

def print_all(f):
		a = f.read()
		print (a)
def rewind(f):
	f.seek(10)
def print_a_line(line_count,f):
	print (line_count,f.readline())
object=open (filename)
print ("现在操作这个文件")
print_all(object)
print ("现在做些其它事情")
rewind(object)
print_a_line(1,object)
print_a_line(2,object)
print_a_line(3,object)

#seek(a)，a为数字，意思是回到文件内容的第几个字符，从0开始计数
#readline()是读取文件的哪一行，每读取一行计数器增加1