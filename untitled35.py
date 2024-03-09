class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def create_tree():
    root_value = int(input("Enter the value for the root node: "))
    root_node = TreeNode(root_value)
    node_queue = [root_node]

    while node_queue:
        current_node = node_queue.pop(0)
        left_value = input(f"Enter the left child value of {current_node.value} (or 'None' if no left child): ")
        if left_value.lower() != 'none':
            current_node.left_child = TreeNode(int(left_value))
            node_queue.append(current_node.left_child)

        right_value = input(f"Enter the right child value of {current_node.value} (or 'None' if no right child): ")
        if right_value.lower() != 'none':
            current_node.right_child = TreeNode(int(right_value))
            node_queue.append(current_node.right_child)

    return root_node

def count_levels(tree):
    if tree is None:
        return 0
    elif tree.left_child is None and tree.right_child is None:
        return 1
    else:
        left_levels = count_levels(tree.left_child) if tree.left_child else 0
        right_levels = count_levels(tree.right_child) if tree.right_child else 0
        return max(left_levels, right_levels) + 1

def main():
    root_node = create_tree()
    num_levels = count_levels(root_node)
    print("Number of levels in the binary tree:", num_levels)

if __name__ == "__main__":
    main()
