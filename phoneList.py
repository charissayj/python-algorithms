#Using a singly-linked list, create a list for phone contacts
class SLNode(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

class SList(object):
	def __init__(self):
		self.head = None
		self.tail = None

list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
list.tail = SLNode("Brad")
print list.head.value
print list.head.next.value
print list.head.next.next.value
print list.tail.value