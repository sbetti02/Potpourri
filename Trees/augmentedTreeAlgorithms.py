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
    """
        Return the rank of the element specified by *key* (1 INDEXED)
        Returns -1 if key does not exist
    """
    node_path = aug_BST.nodes_on_path_to_key(key)
    if not node_path:
        return -1
    last_node = node_path.pop()
    if last_node.left:
        rank = last_node.left.num_sub_nodes + 1
    else:
        rank = 1
    next_node = last_node
    while node_path:
        curr_node = node_path.pop()
        if curr_node.key < next_node.key: # parent's right child
            if curr_node.left:
                rank += curr_node.left.num_sub_nodes+1
            else:
                rank += 1
        next_node = curr_node
    return rank

def dynamic_selection(aug_BST, rank):
    """Return the key of the node with *rank* within the tree"""
    curr_node = aug_BST.root
    while curr_node:
        if curr_node.left:
            curr_rank = curr_node.left.num_sub_nodes+1
        else:
            curr_rank = 1
        if rank == curr_rank:
            return curr_node
        if curr_rank > rank:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
            rank -= curr_rank
    return None

def main():
    T = AugmentedBST()
    to_insert = random.sample(xrange(100), 10)
    T.bulk_insert(to_insert)
    print range_count(T, 20, 30)
    T.print_tree()
    sorted_vals = T.inorder_traversal_r()
    print sorted_vals
    rank = find_rank(T, sorted_vals[5])
    print "\nrank:", rank
    print dynamic_selection(T, 1).key


if __name__ == "__main__":
    main()