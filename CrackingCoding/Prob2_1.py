class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def print_list(head):
	while head is not None:
		print head.val,
		head = head.next
	print ''

# 2.1 Remove duplicates from linked list
def remove_dup(head):
	Prev = None
	Curr = head
	Next = None
	d = []
	while Curr is not None:
		Next = Curr.next
		if Curr.val not in d:
			d.append(Curr.val)
		else:
			Prev.next = Next
			Curr = Next 
		Prev = Curr
		Curr = Next
# 2.2 Delete nth to last element of a singly linked list
def delete_nth(head,n):
	Curr = head
	for i in xrange(n-1):
		Curr = Curr.next
	Prev = None
	Curr2 = head
	while Curr is not None:
		Prev = Curr2
		Curr2 = Curr2.next
		Curr = Curr.next

	Prev.next = Curr2.next

#2.3 Delete a node in a linked list with access only to that node
def delete_node(node):
	Curr = node
	if Curr.next == None:
		Curr.val = None
		print 'Last node'
	else:
		Curr.val = Curr.next.val
		Curr.next = Curr.next.next
# 2.4 add two numbers represented by linked list in reverse order
def addtwonums(l1,l2):
	C1,C2 = l1,l2
	carry = 0
	
	while C1 is not None or C2 is not None or carry != 0:
		if C1 is None:
			P1.next = Node(0)
			C1 = P1.next
		if C2 is None:
			n = C1.val + carry
		else:	
			n = C1.val + C2.val + carry
		carry, C1.val = divmod(n,10)
		'''
		if n >= 10:
			C1.val = n- 10
			carry = 1
		else:
			C1.val = n
			carry = 0
		'''
		P1 = C1
		C1 = C1.next
		if C2 is not None:
			C2 = C2.next






l = [50, 5, 6, 23, 2, 2, 7, 6, 37, 6]
head = Node(1)
Curr = head
for n in l:
	Curr.next = Node(n)
	Curr = Curr.next

print_list(head)
remove_dup(head)
print_list(head)
delete_nth(head,3)
print_list(head)
delete_node(head.next.next.next.next.next.next)
print_list(head)

l1 = Node(3)
l1.next = Node(1)
l1.next.next = Node(5)
l2 = Node(5)
l2.next = Node(9)
l2.next.next = Node(4)
addtwonums(l1,l2)
print_list(l1) 

l1 = Node('A')
l1.next = Node('B')
l1.next.next = Node('C')
l1.next.next.next = Node('D')
l1.next.next.next.next = Node('E')
l1.next.next.next.next.next = l1.next.next = Node('C')





