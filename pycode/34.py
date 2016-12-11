#列表和字典

#列表为中括号，元素加引号(数字和字母除外)，元素之间用逗号分隔开
#字典用大括号，元素索引和内容为一组，索引和元素都加引号，索引后面加冒号，组之间用逗号分隔开

#数组对元素修改的方法：
things = ['one','two','three','four','five',1,2,3,4,5,66*9,72/3,65%3,2**9]
print (things)
things.append(100**9)
print (things)
print (things[0])
print (things[1])
print (things[2])

things[0]="test"
print (things[0])

list = ['1','2']
list.insert(1,6**9)
print (list)



