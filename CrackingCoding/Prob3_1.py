#3.1 use a single array to implement 3 stacks
#3.4 Towers of Hanoi
class Tower:
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

def move_recur(source, dest, spare, disk,l): 
	print 'Update;'
	for t in l:
		t.view()
	if not source.isempty() and disk == source.peek() and (disk < dest.peek() or dest.isempty()):
		dest.push(source.pop())
	else:
		move_recur(source, spare, dest, disk-1, l)
		move_recur(source, dest, spare, disk, l)
		move_recur(spare, dest, source, disk-1, l)

# def move_itr(source, dest, spare, disk): 
# 	if not source.isempty() and disk == source.peek() and (disk < dest.peek() or dest.isempty()):
# 		dest.push(source.pop())
# 		return True
# 	else: return False



nT = 3 # No of Towers
l = [None for i in xrange(nT)]
for i in xrange(nT):
	l[i] = Tower()
m = 5 # No. of disks
for i in xrange(m-1,-1,-1):
	l[0].push(i)

for i in xrange(nT):
	print 'Tower %d:' % i
	l[i].view()

move_recur(l[0],l[1],l[2],m-1,l)


print 'After Moving'
for i in xrange(nT):
	l[i].view()










