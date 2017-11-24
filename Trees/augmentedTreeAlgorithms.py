from augmentedBST import AugmentedBST
import random

def range_count(aug_BST, x, y):
	"""Return the number of elements between x (inclusive) and y"""
	curr_node = aug_BST.root
	while curr_node and not _in_range(curr_node.key, x, y):
		if curr_node.key > y:
			curr_node = curr_node.left
		else:
			curr_node = curr_node.right
	if not curr_node:
		return 0
	return 1 + _left_probe_count(curr_node.left, x, y) + \
	           _right_probe_count(curr_node.right, x, y)


def _in_range(key, x, y):
	"""Determine if the key is in the range between x and y"""
	return key < y and key >= x

def _left_probe_count(node, x, y):
	"""Probe to the left, return how many nodes from the left are within the range"""
	count = 0
	while node:
		if _in_range(node.key, x, y):
			count += 1
			if node.right:
				count += node.right.num_sub_nodes
			node = node.left
		else:
			node = node.right
	return count

def _right_probe_count(node, x, y):
	"""Probe to the right, return how many nodes from the right are within the range"""
	count = 0
	while node:
		if _in_range(node.key, x, y):
			count += 1
			if node.left:
				count += node.left.num_sub_nodes
			node = node.right
		else:
			node = node.left
	return count
	

def find_rank(aug_BST, key):
	"""Return the rank of the element specified by *key*"""
	pass

def dynamic_selection(aug_BST, rank):
	"""Return the key of the node with *rank* within the tree"""
	pass


def main():
	T = AugmentedBST()
	to_insert = random.sample(xrange(100), 10)
	T.bulk_insert(to_insert)
	print range_count(T, 20, 30)
	to_insert = sorted(to_insert)
	print to_insert


if __name__ == "__main__":
	main()