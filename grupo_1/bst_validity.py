class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.key < max_val):
        return False
    return (is_valid_bst(node.left, min_val, node.key) and
            is_valid_bst(node.right, node.key, max_val))

if __name__ == "__main__":
    # Exemplo construindo uma BST válida
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    print("Árvore válida?", is_valid_bst(root))

    # Caso inválido: forçamos um nó fora do lugar
    root.left.right.key = 100
    print("Árvore válida após alteração?", is_valid_bst(root))
