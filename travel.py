from collections import deque


def pre_order(node):  # Прямой обход
    if node:
        print(node.key, end=" ")
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):  # Симметричный обход
    if node:
        in_order(node.left)
        print(node.key, end=" ")
        in_order(node.right)


def post_order(node):  # Обратный обход
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.key, end=" ")


def level_order(node):  # Обход в ширину
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.key, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
