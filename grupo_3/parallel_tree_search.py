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

def parallel_search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(parallel_search, root.left, target)
        right_future = executor.submit(parallel_search, root.right, target)
        return left_future.result() or right_future.result()

if __name__ == "__main__":
    # Construção de exemplo
    values = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for v in values:
        root = insert(root, v)
    target = 60
    found = parallel_search(root, target)
    print(f"Valor {target} encontrado?", found)
