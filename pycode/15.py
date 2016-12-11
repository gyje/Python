from sys import argv
script ,filename=argv
text=open (filename)
print ("文件名称是%s" % filename)
print ("文件内容是%s" % text.read())
print ("让我们重新打开文件")
file = input("输入文件名称")
print (open(file).read())