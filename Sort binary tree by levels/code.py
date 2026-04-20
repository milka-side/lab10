def tree_by_levels(node):
    if not node: return []
    queue = [node]
    tree = []
    while queue:
        node = queue.pop(0)
        tree.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return tree
