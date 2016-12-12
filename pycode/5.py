

a = "hello"
b = 100
c = 5<6
d = [1,2,3,4,5,6]

print ("%s" % a)
print ("%s,%d" % (a,b))
print (a)
print (a,b)
print ("%s,%s,%s,%s" % (a,b,c,d))
print (a,b,c,d)

b = "test%rmode\n\n\n\n\t\t\t"
print ("%s" % b)
print ("%r" % b)
print ("test%rmode\n\n\n\n\t\t\t")


#总之，%s代表字符串，%d是数字，%r是调试模式，%不需要转义，%r模式下转义字符没有用