from collections import deque

class BST(object):
    """Basic representation of a Binary Tree for practicing tree rotations"""
    root = None

    def __init__(self):
        """Initialize tree with NULL root node"""
        self.node_class = Node

    def bulk_insert(self, key_list):
        """Insert a list of keys into BST"""
        for key in key_list:
            self.insert_node(key)

    def insert_node(self, key):
        """
            Insert node to the tree with value *key*
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
        while curr_node:
            prev_node = curr_node
            if key == curr_node.key:
                return None
            if key > curr_node.key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        inserting = self.node_class(key)
        if key > prev_node.key:
            prev_node.right = inserting
        else:
            prev_node.left = inserting
        return inserting

    def find_node(self, key):
        """Find and return the node with value *key* if it exists"""
        if not self.root:
            return None
        parent_node = None
        node = self.root
        while node and not node.key == key:
            parent_node = node
            if key > node.key:
                node = node.right
            else:
                node = node.left
        return node

    def _find_node_and_parent(self, key):
        """Locate a node by *key* val and return it and its parent if they exist"""
        if not self.root:
            return None, None
        parent_node = None
        node = self.root
        while node and not node.key == key:
            parent_node = node
            if key > node.key:
                node = node.right
            else:
                node = node.left
        return node, parent_node

    # Rotate tree right and left

    """
         A                    B
       /   \       <==>      / \ 
      B     Z      <==>     X   A
     / \           <==>        / \ 
    X  Y                      Y   Z
    """


    def rotate_right(self, key):
        """ 
            Rotate right at the node found by key.
            Checks for NULL node or left child
            Reattaches rotated piece back into tree.
        """
        node, parent = self._find_node_and_parent(key)
        if not node or not node.left: # Inoperable rotation
            return 
        B = node.left
        node.left = B.right
        B.right = node
        if not parent: # Rotating root
            self.root = B
        else:
            if B.key > parent.key: # right child of parent
                parent.right = B
            else:
                parent.left = B

    def rotate_left(self, key):
        """
            Rotate left at the node found by key.
            Checks for NULL node or right child
            Reattaches rotated piece back into tree.
        """
        node, parent = self._find_node_and_parent(key)
        if not node or not node.right:
            return
        A = node.right
        node.right = A.left
        A.left = node
        if not parent: # rotating root
            self.root = A
        else:
            if A.key > parent.key: # right child of parent
                parent.right = A
            else:
                parent.left = A

    def rotate_root_left(self):
        """Rotate the root to the left.  Doesn't spend time to find node."""
        node = self.root
        if not node or not node.right:
            return
        A = node.right
        node.right = A.left
        A.left = node
        self.root = A

    def rotate_root_right(self):
        """Rotate the root to the right.  Doesn't spend time to find node."""
        node = self.root
        if not node or not node.left:
            return
        B = node.left
        node.left = B.right
        B.right = node
        self.root = B

    @staticmethod
    def _find_min_using_parent(node, parent):
        if not node or not node.left:
            return node, parent
        while node.left:
            parent = node
            node = node.left
        return node, parent

    @staticmethod
    def _delete_node_without_both_children(node, parent):
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
        return

    def delete_node(self, key):
        """Delete node with value *key*"""
        node, parent = self._find_node_and_parent(key)
        if not node:
            return
        if not parent: # deleting root node
            if node.left:
                self.rotate_root_right()
            elif node.right:
                self.rotate_root_left()
            else:
                self.root = None
                return
            parent = self.root
        if not node.left or not node.right:
            self._delete_node_without_both_children(node, parent)
        else:
            min_right, min_right_parent = self._find_min_using_parent(node.right, node)
            node.key = min_right.key
            self._delete_node_without_both_children(min_right, min_right_parent)
        return

    @staticmethod
    def _print_tree_level(print_list, level):
        """ 
            Print out the nodes *level* down from the root, space delimited, 
            printing 'x' where values do not appear on the tree.
        """
        if not print_list:
            return
        num_elems = 2**level
        print_list_len = len(print_list)
        for i in xrange(print_list_len, num_elems):
            print_list.append('x')
        print (' ').join(print_list)

    def print_tree(self):
        """ 
            Print the levels of a tree space delimited, printing 'x' where values
            do not appear on the tree.
            *print_list* contains the list we want to print out
            *to_explore* contains all nodes going to explore, stored as 
            [(node, pos_in_arr, lev),...,] in a double-ended queue (deque)
        """
        if not self.root:
            return
        to_explore = deque()
        to_explore.append((self.root, 0, 0))
        print_list = []
        level = -1

        while to_explore:
            curr_node, arr_pos, curr_level = to_explore.popleft() # optimized with queue
            if curr_level == level:
                for i in xrange(len(print_list), arr_pos):
                    print_list.append('x')
            else:
                self._print_tree_level(print_list, level)
                level += 1
                print_list = []
                for i in xrange(0, arr_pos):
                    print_list.append('x')
            print_list.append(str(curr_node.key))
            if curr_node.left:
                to_explore.append((curr_node.left, arr_pos*2, curr_level+1))
            if curr_node.right:
                to_explore.append((curr_node.right, (arr_pos*2)+1, curr_level+1))
        self._print_tree_level(print_list, level)

    def nodes_on_path_to_key(self, key):
        """
            Return a list of the nodes on the path to the node specified by *key* or None
            if the node does not exist
        """
        node_list = []
        node = self.root
        while node and node.key != key:
            node_list.append(node)
            if node.key > key:
                node = node.left
            else:
                node = node.right
        if not node:
            return None
        node_list.append(node)
        return node_list

    def preorder_traversal_s(self):
        """Preorder traverse the tree through use of a stack instead of recursively"""
        if not self.root:
            return []
        stack = [self.root]
        traversed = []
        while stack:
            curr_node = stack.pop()
            traversed.append(curr_node.key)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        return traversed

    def preorder_traversal_r(self):
        """Recursively return list with exploring tree in manner of self, left child, right child"""
        return self._preorder_traversal_r_helper(self.root)

    def _preorder_traversal_r_helper(self, curr_node):
        """Recursively return list with exploring tree in manner of self, left child, right child"""
        if not curr_node:
            return []
        preorder_traversed = [curr_node.key]
        preorder_traversed.extend(self._preorder_traversal_r_helper(curr_node.left))
        preorder_traversed.extend(self._preorder_traversal_r_helper(curr_node.right))
        return preorder_traversed

    def inorder_traversal_s(self):
        """Simulate recursive inorder traversal using a stack"""
        if not self.root:
            return []
        stack = [self.root]
        traversed = []
        already_processed = set()
        while stack:
            curr_node = stack[-1]
            if curr_node.right and curr_node.right.key not in already_processed:
                already_processed.add(curr_node.right.key)
                curr_node = stack.pop()
                stack.append(curr_node.right)
                stack.append(curr_node)
            if curr_node.left and curr_node.left.key not in already_processed:
                stack.append(curr_node.left)
            else:
                popped = stack.pop()
                already_processed.add(popped.key)
                traversed.append(popped.key)
        return traversed

    def inorder_traversal_r(self):
        """Recursively return list with exploring left child, then self, then right child"""
        return self._inorder_traversal_r_helper(self.root)

    def _inorder_traversal_r_helper(self, curr_node):
        """Recursively return list with exploring left child, then self, then right child"""
        if not curr_node:
            return []
        ordered_list = self._inorder_traversal_r_helper(curr_node.left)
        ordered_list.append(curr_node.key)
        ordered_list.extend(self._inorder_traversal_r_helper(curr_node.right))
        return ordered_list

    def postorder_traversal_s(self):
        """Simulate recursive inorder traversal using a stack"""
        if not self.root:
            return []
        processed = set()
        traversed = []
        stack = [self.root]
        while stack:
            curr_node = stack[-1]
            append_node = True
            if curr_node.right and curr_node.right.key not in processed:
                stack.append(curr_node.right)
                processed.add(curr_node.right.key)
                append_node = False
            if curr_node.left and curr_node.left.key not in processed:
                stack.append(curr_node.left)
                processed.add(curr_node.left.key)
                append_node = False
            if append_node:
                traversed.append(stack.pop().key)
        return traversed

    def postorder_traversal_r(self):
        """Recursively return list with exploring left child, right child, then self"""
        return self._postorder_traversal_r_helper(self.root)

    def _postorder_traversal_r_helper(self, node):
        """Recursively return list with exploring left child, right child, then self"""
        if not node:
            return []
        postorder_traversed = self._postorder_traversal_r_helper(node.left)
        postorder_traversed.extend(self._postorder_traversal_r_helper(node.right))
        postorder_traversed.append(node.key)
        return postorder_traversed

class Node(object):
    """
        Representation of a node on a tree containing a value and left/right pointers
        to start, may later include more information if incorporated into an
        augmented tree
    """
    key = None
    left = None
    right = None

    def __init__(self, value):
        """
            Initialize an empty node with *value* and no left/right pointers.
            Update to augment node for more metadata in tree.
        """
        self.key = value

def main():
    T = BST()
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
    print T.inorder_traversal_s()
    print T.preorder_traversal_r()
    print T.preorder_traversal_s()
    print T.postorder_traversal_r()
    print T.postorder_traversal_s()
    T.rotate_right(3)
    T.print_tree()
    T.insert_node(8.3)
    T.print_tree()
    T.delete_node(10)
    T.print_tree()
    T.delete_node(8)
    T.print_tree()
    T.delete_node(5)
    T.print_tree()
    T.delete_node(11)
    T.print_tree()
    for i in range(11):
        T.delete_node(i)
        T.print_tree()
    T.delete_node(4.5)
    T.print_tree()
    T.delete_node(8.3)
    T.print_tree()
    for i in range(5):
        T.insert_node(i)
    T.print_tree()
    T.insert_node("asdf")
    T.print_tree()

if __name__ == "__main__":
    main()


