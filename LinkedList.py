# LinkedList
# O(n) ~ 
class LinkedList:
	first = None 
	# Method description 
	# O(n) ~
	def __init__(self):
		pass
	
	def __init__(self, value):
		first = Node(value)
	
	class Node:
		self.value = 0
		self.next = None
		
		def __init__(self, value):
			self.value = value
		
		
	def add(self, x):
		if self.first is None:
			self.first = Node(x)
			return self.first
		
		iterator = self.first
		while iterarot.next is not None:
			iterator = iterator.next
		
		iterator.next = Node(x)
		
	def remove(self, x):
		pass		 
	 
	def get(self, x):
		iterator = self.first
		#while iterator.va != 
	
	

