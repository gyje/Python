def print_tab(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_tab(each_item)
		else:
			print(each_item)

list1=["1","2",'3','test',[1,2,3],100*6]		
print_tab(list1)	