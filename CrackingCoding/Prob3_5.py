#3.5 implement a MyQueue clas which implements a queue using two stacks
class stack:
	def __init__(self):
		self.items = []

	def isempty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.isempty():
			return self.items.pop()
		return None
	def peek(self):
		if self.size() >0:
			return self.items[-1]
		return None

	def size(self):
		return len(self.items)

	def view(self):
		print self.items

class MyQueue:
	def __init__(self):
		self.stack1 = stack()
		self.stack2 = stack()

	def enqueue(self, item):
		self.stack1.push(item)

	def dequeue(self):
		if self.stack2.isempty():
			while not self.stack1.isempty():
				self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

	def size(self):
		return self.stack1.size() + self.stack2.size()
# 3.6 Sort a stack in ascending order using only push,pop, peek, isempty
def sort_stack(s1):
	s2 = stack()
	while not s1.isempty():
		n = s1.pop()
		if s2.isempty():
			s2.push(n)
		else:
			while( not s2.isempty() and s2.peek() > n):
				s1.push(s2.pop())
			s2.push(n)
	return s2






q = MyQueue()
l = [1, 2, 3 ,4 ,5, 6, 7, 8]
for i in l:
	q.enqueue(i)
while q.size() >0 :
	print q.dequeue()
	
l1 = [2, 5, 3, 9, 4, 11, 6]
s = stack()
for i in l1:
	s.push(i)
s.view()
s2 = sort_stack(s)
s2.view()










