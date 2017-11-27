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


class Node(object):
	"""Basic implementation of a node on a singly linked list"""

	def __init__(self, key):
		self.key = key
		self.next = None


def main():
	link_list = LinkedList()
	link_list.append_node(3)
	link_list.append_node(6)
	link_list.append_node(2)
	link_list.prepend_node(10)
	link_list.prepend_node(8)
	link_list.print_list()
	link_list.delete_node(8)
	link_list.print_list()
	print link_list.find_node(3).key

if __name__ == "__main__":
	main()








