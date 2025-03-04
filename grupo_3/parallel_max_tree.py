import concurrent.futures

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def parallel_find_max(root):
    if not root:
        return float('-inf')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(parallel_find_max, root.left)
        right_future = executor.submit(parallel_find_max, root.right)
        left_max = left_future.result()
        right_max = right_future.result()
    return max(root.value, left_max, right_max)

if __name__ == "__main__":
    # Construção de exemplo
    values = [15, 10, 20, 8, 12, 17, 25]
    root = None
    for v in values:
        root = insert(root, v)
    max_val = parallel_find_max(root)
    print(f"Valor máximo na árvore:", max_val)
