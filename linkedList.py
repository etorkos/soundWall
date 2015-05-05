
class Node(object):
	#__init__ roughly a JS constructor
	def __init__(self, value):
		self.value = value;
		self.count = 0
		self.next = None
		
class linkedList(object):
	#head=None is a default
	def __init__(self, head=None):
		self.head = head
		
	def insert(self, node):
		if not self.head:
			self.head = node
		else:
			inserted = "false"
			front = self.head
			if node.value >= self.head.value:
				self.head = node
			else:
				while inserted == "false":
					if front.next is not None:
						if node.value < front.next.value:
							front = front.next
						else:
							front.next = node
							inserted = "true"
					else:
						front.next = node
						inserted = "true"
	
	def update(self):
		finished = "false"
		front = self.head
		while finished == "false":
			if front.count >= 7:
				stuff
				
			else:
				front.count = front.count + 1
				front = front.next
					
	def delete(self):
		if self.head is not None:
			print "Removing"
			print self.head
			self.head = self.head.next
		
		
myList = linkedList()
node1 = Node(5)
node2 = Node(7)
myList.insert(node1)
myList.insert(node2)
myList.delete()
