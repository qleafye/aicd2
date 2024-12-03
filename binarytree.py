class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Поиск
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Удаление
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Узел с одним или без потомков
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Узел с двумя потомками
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_recursive(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def calculate_height(self, node):
        if node is None:
            return -1
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return max(left_height, right_height) + 1

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            # Рекурсивно обходим правое поддерево
            self.print_tree(node.right, level + 1, "R----")
            # Печатаем текущий узел с отступами
            print(" " * (level * 6) + prefix + str(node.key))
            # Рекурсивно обходим левое поддерево
            self.print_tree(node.left, level + 1, "L----")