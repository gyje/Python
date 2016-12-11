#字典
cite={"yuansu1":"1","yuansu2":"2",'yuansu3':'3',"4":"ys4"}

print (cite)
print (cite['yuansu1'])


cite['yuansu3']='4'
print (cite['yuansu3'])
print (cite["4"])

del cite['yuansu1']
print (cite)

cite["s4"]="yuansu4"
print (cite)
#要记住，字典中中括号索引的内容必须是字典中有的内容，否则，会报错，索引中的数字例如1，2，3，4，并不是第几个，而是字典中有的键
#字典中的元素是以键值对的形式出现的
'''这块代码有误'''
for cite in cite.items():
	print ("%s" % cite)