class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=" ")

if __name__ == "__main__":
    bst = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print("In-order:", end=" ")
    bst.inorder()
    print("Pre-order:", end=" ")
    bst.preorder()
    print("Post-order:", end=" ")
    bst.postorder()
