from sys import argv
from os.path import exists

script,from_file,to_file=argv

print ("文件1的存在状态 %s" % exists(from_file))
print ("文件2的存在状态 %s" % exists(to_file))

fileobject1=open (from_file)

#print ("文件1 中 一共有 %d 个字符" % len(fileobject1.read()))
#print ("文件2 中 一共有 %d 个字符" % len(fileobject2.read()))

print ("我们要做的是，把文件1的内容 复制到 文件2 中去")

input(">>>>>>>>>>>>>>>>>>>>>>>>>>")

a = fileobject1.read()

open (to_file,"w").write(a)

print ("现在文件1中内容是 %r" % a)
print ("现在文件2中内容是 %s" % open(to_file).read())

fileobject1.close()




