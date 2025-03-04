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

def parallel_dfs_path(root, target):
    if not root:
        return []
    if root.value == target:
        return [root.value]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(parallel_dfs_path, root.left, target)
        right_future = executor.submit(parallel_dfs_path, root.right, target)
        left_path = left_future.result()
        right_path = right_future.result()
    if left_path:
        return [root.value] + left_path
    if right_path:
        return [root.value] + right_path
    return []

if __name__ == "__main__":
    # Construção de exemplo
    values = [1, 2, 3, 4, 5, 6, 7]
    root = None
    for v in values:
        root = insert(root, v)
    target = 5
    path = parallel_dfs_path(root, target)
    print(f"Caminho até {target}:", path)
