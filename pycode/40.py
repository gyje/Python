class people :#定义一个类。相当于写了一个名字为people的工程蓝图


		def speak(self):#这个名为people的蓝图中，能有speak()这个东西
			print ("我会说话")
		def eat(self):
			print ("我会吃饭")
		def play(self):
			print ("我会玩")


xiaoming=people()#根据蓝图把xiaoming造出来了，xiaoming就是一个实例化的对象
xiaoming.speak()#因为只要是根据蓝图造的东西就有蓝图中的功能，所以xiaoming能有speak这个功能，下面同理。
xiaoming.eat()
xiaoming.play()















#再次深入探究：
class people():#创建一个工程图
		def __init__(self,name,age,sex):#注意这里init左右两边都是两个短下划线
		#self是必须有的参数
		#工程图
		
			


		

		

		
