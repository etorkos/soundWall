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
		previous = None
		while finished == "false":
			if front is None:
				finished = 'true'
			elif front.count >= 9:
				if previous is not None:
					previous.next = front.next
					front = front.next
				else:
					self.head = front.next
					front = front.next
			else:
				front.count = front.count + 1
				front = front.next
					
	def report(self):
		finished = 'false'
		node = self.head
		count = 0
		while finished == 'false':
			if node is not None:
				print "location %s, value: %s, time in QUEUE, %s" % (count, node.value, node.count) 
				count = count + 1
				node = node.next
			else:
				print "\n"
				finished = 'true'
		
	def cycle(self, value):
		newNode = Node(value)
		self.update()
		self.insert(newNode)

	def frontNodeValue(self):
		return self.head.value




