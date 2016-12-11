from sys import argv
script,filename= argv
print ("我们将要打开的文件名称是 %r" % filename)
print ("我们将要打开的文件名称是 %s" % filename)
print ("现在文件内容是：\n")
fileobject = open (filename)
print (fileobject.read())

print ("如果要退出程序请按ctrl+c,继续请按任意键")
input (">>>>>>>>>>>>>>>>>>>>")

print ("接下来清空文件内容")
fileobject=open (filename,"w")

line1=input("请输入第一行内容")
line2=input ("请输入第二行内容")
line3=input ("请输入第三行内容")

print ("现在我将要把你输入的内容写入到打开的文件中")

fileobject.write(line1)
fileobject.write ("\n")
fileobject.write (line2)
fileobject.write ("\n")
fileobject.write (line3)
fileobject.write ("\n")

fileobject=open (filename)
print ("现在文件内容是 %s" % fileobject.read())
print ("最后关闭文件")

fileobject.close()



