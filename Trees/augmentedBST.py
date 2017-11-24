from binarySearchTree import BST
from binarySearchTree import Node

class AugmentedBST(BST):
    def __init__(self):
        """Initialize a node_class, used in the current implementation of insert"""
        self.node_class = AugmentedNode

    def insert_node(self, key):
        """
            Insert node to the tree with value *key*
            Increment num_sub_nodes on every node passed
            Check to ensure key is unique
            Return the inserted node
            Returns None if key cannot be inserted
        """
        if not isinstance(key, (int, float, long)):
            print "Cannot insert", key
            return None
        if not self.root:
            self.root = self.node_class(key)
            return self.root

        prev_node = None
        curr_node = self.root
        incremented_nodes = []
        while curr_node:
            prev_node = curr_node
            incremented_nodes.append(prev_node)
            if key == curr_node.key:
                return None
            if key > curr_node.key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        for node in incremented_nodes:
            node.increment_sub_tree()
        inserting = self.node_class(key)
        if key > prev_node.key:
            prev_node.right = inserting
        else:
            prev_node.left = inserting
        return inserting

    def rotate_right(self, key):
        """ 
            Rotate right at the node found by key.
            Checks for NULL node or left child
            Modify subtree counts appropriately
            Reattaches rotated piece back into tree.
        """
        node, parent = self._find_node_and_parent(key)
        if not node or not node.left: # Inoperable rotation
            return
        B = node.left
        node.left = B.right
        if B.left:
            node.decrement_sub_tree(B.left.num_sub_nodes) # Remove count for node not on subtree
        node.decrement_sub_tree() # Account for B
        B.right = node
        if node.right:
            B.increment_sub_tree(node.right.num_sub_nodes)
        B.increment_sub_tree() # Account for node itself
        if not parent: # Rotating root
            self.root = B
        else:
            if B.key > parent.key: # right child of parent
                parent.right = B
            else:
                parent.left = B

    def rotate_root_right(self):
        """
            Rotate the root to the right.  Doesn't spend time to find node.
            Modify subtree counts appropriately
        """
        node = self.root
        if not node or not node.left:
            return
        B = node.left
        node.left = B.right
        if B.left:
            node.decrement_sub_tree(B.left.num_sub_nodes)
        node.decrement_sub_tree() # Account for B
        B.right = node
        if node.right:
            B.increment_sub_tree(node.right.num_sub_nodes)
        B.increment_sub_tree() # Account for node
        self.root = B

    def rotate_left(self, key):
        """
            Rotate left at the node found by key.
            Checks for NULL node or right child
            Modify subtree counts appropriately
            Reattaches rotated piece back into tree.
        """
        node, parent = self._find_node_and_parent(key)
        if not node or not node.right:
            return
        A = node.right
        node.right = A.left
        if A.right:
            node.decrement_sub_tree(A.right.num_sub_nodes)
        node.decrement_sub_tree() # Account for A
        A.left = node
        if node.left:
            A.increment_sub_tree(node.left.num_sub_nodes)
        A.increment_sub_tree() # Account for the node itself
        if not parent: # rotating root
            self.root = A
        else:
            if A.key > parent.key: # right child of parent
                parent.right = A
            else:
                parent.left = A

    def rotate_root_left(self):
        """
            Rotate the root to the left.  Doesn't spend time to find node.
            Modify subtree counts appropriately
        """
        node = self.root
        if not node or not node.right:
            return
        A = node.right
        node.right = A.left
        if A.right:
            node.decrement_sub_tree(A.right.num_sub_nodes)
        node.decrement_sub_tree() # Account for A
        A.left = node
        if node.left:
            A.increment_sub_tree(node.left.num_sub_nodes)
        A.increment_sub_tree() # Account for node
        self.root = A

    def _decrement_subtree_counts_to_node(self, last_decremented_node):
        curr_node = self.root
        last_decremented_key = last_decremented_node.key
        last_decremented_node.decrement_sub_tree()
        while curr_node.key != last_decremented_key:
            curr_node.decrement_sub_tree()
            if curr_node.key > last_decremented_key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def _delete_node_without_both_children(self, node, parent):
        """Delete function without both children under the assumption the parent exists"""
        if not node.left:
            if parent.key > node.key:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            if parent.key > node.key:
                parent.left = node.left
            else:
                parent.right = node.left
        self._decrement_subtree_counts_to_node(parent)
        return

class AugmentedNode(Node):
    """
        Representation of a node on a tree containing a value and left/right pointers
        to start, as well as the number of nodes on a subtree with the root at that
        node
    """

    def __init__(self, value):
        """
            Initialize an empty node with *value* and left/right pointers set to None.
            *self.num_sub_nodes* used for various algorithms.
        """
        self.key = value
        self.num_sub_nodes = 1

    def increment_sub_tree(self,val=1):
        """Increment the number of sub nodes by *val*"""
        self.num_sub_nodes += val

    def decrement_sub_tree(self, val=1):
        """Decrement the number of sub nodes by *val*"""
        self.num_sub_nodes -= val

def test_subtree_counts(node):
    if not node:
        return True
    if not node.right and not node.left:
        return node.num_sub_nodes == 1
    if not node.right:
        return node.num_sub_nodes == node.left.num_sub_nodes+1 and \
               test_subtree_counts(node.left)
    if not node.left:
        return node.num_sub_nodes == node.right.num_sub_nodes+1 and \
               test_subtree_counts(node.right)
    return node.num_sub_nodes == node.left.num_sub_nodes + node.right.num_sub_nodes + 1 and \
           test_subtree_counts(node.left) and test_subtree_counts(node.right)

def main():
    T = AugmentedBST()
    T.insert_node(5)
    T.insert_node(6)
    T.insert_node(3)
    T.insert_node(7)
    T.insert_node(1)
    for i in range(11):
        T.insert_node(i)
    T.insert_node(4.5)
    T.print_tree()
    print T.inorder_traversal_r()
    print T.preorder_traversal_r()
    print T.postorder_traversal_r()
    print "Subtree counts working...", test_subtree_counts(T.root)
    T.rotate_right(5)
    print "Subtree counts working...", test_subtree_counts(T.root)
    T.rotate_left(1)
    print "Subtree counts working...", test_subtree_counts(T.root)
    T.print_tree()
    T.rotate_root_left()
    print "Subtree counts working...", test_subtree_counts(T.root)
    T.print_tree()
    T.print_tree()
    T.insert_node(8.3)
    T.print_tree()
    T.delete_node(10)
    T.print_tree()
    T.delete_node(8)
    T.print_tree()
    #print "Subtree counts working...", test_subtree_counts(T.root)
    #print T.find_node(6).num_sub_nodes


if __name__ == "__main__":
    main()