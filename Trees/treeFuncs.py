## If there's nothing at the root, add the node with no left or 
## right child to the root
## If there is, if value is less than root, recurse on left child,
## otherwise recurse on right child.  Go until child reached is None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root:
            if self.root.value() < val:
                return self.addHelper(val, self.root.rightChild, self.root)
            else:
                return self.addHelper(val, self.root.leftChild, self.root)
        else:
            self.root = TreeNode(val)
            return 1

    def addHelper(self, val, currNode, parent):
        if not currNode:
            parent.addChild(TreeNode(val))
            parent.addChild(TreeNode(val))
            return 1
        if currNode.value() < val:
            return self.addHelper(val, currNode.rightChild, currNode)
        return self.addHelper(val, currNode.leftChild, currNode)

    def printTree(self):
        self.printNodes([self.root])

    def printNodes(self, nodeList):
        if nodeList == []:
            return
        childList = []
        for node in nodeList:
            print node.value(),
            print " ",
            if node.leftChild:
                childList.append(node.leftChild)
            if node.rightChild:
                childList.append(node.rightChild)
        print "\n"
        self.printNodes(childList)


class TreeNode:
    def __init__(self, val):
        self.val = val
        #self.parent
        self.leftChild = None
        self.rightChild = None

    def value(self):
        return self.val

    def addChild(self, node):
        if self.val < node.value():
            self.rightChild = node
        else:
            self.leftChild = node

def main():
    bTree = BinaryTree()
    bTree.add(5)
    bTree.add(7)
    bTree.add(4)
    bTree.add(6)
    bTree.add(9)
    bTree.add(1)
    bTree.add(2)
    bTree.printTree()

if __name__ == "__main__":
    main()
