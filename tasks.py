class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.value

def visualize_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            visualize_tree(root.left, level + 1, "L-- ")
            visualize_tree(root.right, level + 1, "R-- ")

# Приклад створення дерева та його заповнення значеннями
def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(10)
    root.left.left.left = TreeNode(1)
    root.right.right.right = TreeNode(12)
    return root

def tree_sum(root):
    if not root:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


def find_min_value(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.value

# Виклик функції для візуалізації створеного дерева
tree_root = build_tree()
visualize_tree(tree_root)
# Task 1
max_value = find_max_value(tree_root)
print("Найбільше значення в дереві:", max_value)
# Task 2
min_value = find_min_value(tree_root)
print("Найменше значення в дереві:", min_value)
# Task 3
sum_of_values = tree_sum(tree_root)
print("Сума всіх значень в дереві:", sum_of_values)