class LinkedList(object):
	"""Basic implementation of a singly linked list"""

	root = None

	def append_node(self, key):
		"""Add a node to the end of the linked list"""
		new_node = Node(key)
		if not self.root:
			self.root = new_node
			return
		node = self.root
		prev = None
		while node:
			prev = node
			node = node.next
		prev.next = new_node

	def prepend_node(self, key):
		"""Add node to front of linked list"""
		new_node = Node(key)
		new_node.next = self.root
		self.root = new_node

	def delete_node(self, key):
		"""Delete the node specified by *key* if it exists, otherwise return None"""
		if not self.root:
			return None
		if self.root.key == key:
			removed_node = self.root.key
			self.root = self.root.next
			return removed_node
		node = self.root
		prev = None
		while node:
			if node.key == key:
				prev.next = node.next
				return
			prev = node
			node = node.next
		return None

	def find_node(self, key):
		"""Find the node specified by *key* if it exists, otherwise return None"""
		node = self.root
		while node:
			if node.key == key:
				return node
			node = node.next
		return None

	def print_list(self):
		"""Print the keys of nodes on the list delimited by => """
		if self.root:
			print self.root.key,
		else:
			return
		node = self.root.next
		while node:
			print " => " + str(node.key),
			node = node.next
		print ""

	def reverse(self):
		"""Reverse the contents of the linked list"""
		if not self.root:
			return
		prev = None
		curr_node = self.root
		while curr_node:
			self.print_list()
			next = curr_node.next
			curr_node.next = prev
			prev = curr_node
			curr_node = next
		self.root = prev


class DoublyLinkedList(LinkedList):
	"""Basic implementation of a doubly linked list"""

	def append_node(self, key):
		"""Append a node to the end of the list"""
		new_node = DoublyLinkedNode(key)
		if not self.root:
			self.root = new_node
			return
		curr = self.root
		prev = None
		while curr:
			prev = curr
			curr = curr.next
		prev.next = new_node
		new_node.prev = prev

	def prepend_node(self, key):
		"""Prepend a node to the beginning of the list"""
		new_node = DoublyLinkedNode(key)
		if not self.root:
			self.root = new_node
			return
		old_root = self.root
		new_node.next = old_root
		old_root.prev = new_node
		self.root = new_node

	def delete_node(self, key):
		"""Delete the node indicated by *key* and return it or None if doesn't exist"""
		if not self.root:
			return None
		curr = self.root
		prev = None
		while curr and curr.key != key:
			prev = curr
			curr = curr.next
		if not curr:
			return None
		if prev:
			prev.next = curr.next
		else:
			self.root = curr.next
		if curr.next:
			curr.next.prev = prev
		return curr

	def reverse(self):
		"""Reverse the contents of a doubly linked list"""
		curr = self.root
		prev = None
		while curr:
			old_next = curr.next
			curr.prev = old_next
			curr.next = prev
			prev = curr
			curr = old_next
		self.root = prev

class Node(object):
	"""Basic implementation of a node on a singly linked list"""

	next = None

	def __init__(self, key):
		self.key = key


class DoublyLinkedNode(Node):
	"""Basic implementation of a doubly linked list node"""

	prev = None


def main():
	link_list = LinkedList()
	link_list.append_node(3)
	link_list.append_node(6)
	link_list.append_node(2)
	link_list.prepend_node(10)
	link_list.prepend_node(8)
	link_list.print_list()
	link_list.reverse()
	link_list.print_list()
	link_list.delete_node(8)
	link_list.print_list()
	print link_list.find_node(3).key
	link_list.delete_node(2)
	link_list.print_list()
	link_list.delete_node(6)
	link_list.print_list()
	print "\n\n\n\n"
	d_ll = DoublyLinkedList()
	d_ll.append_node(6)
	d_ll.append_node(8)
	d_ll.prepend_node(2)
	d_ll.prepend_node(7)
	d_ll.append_node(19)
	d_ll.print_list()
	d_ll.reverse()
	d_ll.print_list()
	d_ll.delete_node(7)
	d_ll.print_list()
	d_ll.delete_node(2)
	d_ll.print_list()
	d_ll.delete_node(19)
	d_ll.print_list()
	d_ll.delete_node(6)
	d_ll.print_list()
	d_ll.delete_node(8)
	d_ll.print_list()


if __name__ == "__main__":
	main()








