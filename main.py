from binarytree import BinarySearchTree
from avltree import AVLTree
from redblacktree import RedBlackTree
from travel import pre_order, in_order, post_order, level_order
import random
import numpy as np
import matplotlib.pyplot as plt


def find_tree_dependence():
    n = []
    h_avl = []
    h_rb = []
    h_bst = []

    bst = BinarySearchTree()

    for i in range(1, 101):

        for _ in range(100):
            while True:
                num = random.randint(0, 10000)
                if not bst.search(num):
                    bst.insert(num)
                    break

        height = bst.calculate_height(bst.root)

        h_bst.append(height)

    for i in range(1, 101):
        keys = list(range(1, 100 * i + 1))

        # AVL
        avl = AVLTree()
        for key in keys:
            avl.insert_key(key)
        h_avl.append(avl.calculate_height(avl.root))

        rb = RedBlackTree()
        for key in keys:
            rb.insert(key)
        h_rb.append(rb.calculate_height(rb.root))

        n.append(100 * i)

    coefficients1 = np.polyfit(n, h_bst, 2)
    coefficients2 = np.polyfit(n, h_avl, 2)
    coefficients3 = np.polyfit(n, h_rb, 2)

    polynomial1 = np.poly1d(coefficients1)
    polynomial2 = np.poly1d(coefficients2)
    polynomial3 = np.poly1d(coefficients3)

    equation1 = f"h = {coefficients1[0]:.10f}n² + {coefficients1[1]:.6f}n + {coefficients1[2]:.2f}"
    equation2 = f"h = {coefficients2[0]:.10f}n² + {coefficients2[1]:.6f}n + {coefficients2[2]:.2f}"
    equation3 = f"h = {coefficients3[0]:.10f}n² + {coefficients3[1]:.6f}n + {coefficients3[2]:.2f}"

    x_fit = np.linspace(min(n), max(n), 500)

    y_fit1 = polynomial1(x_fit)
    y_fit2 = polynomial2(x_fit)
    y_fit3 = polynomial3(x_fit)

    plt.figure(1)
    plt.plot(x_fit, y_fit1, color="red", label=f"Регрессионный полином {equation1}", linestyle=':')
    plt.step(n, np.log2(n), label='Зависимость h = log(n)', color='blue', linestyle='--', where='post')
    plt.step(n, h_bst, label='Зависимость высоты от ключей (BST)', color='green')
    plt.xlabel('Количество ключей')
    plt.ylabel('Высота дерева')
    plt.title('Зависимость высоты BST от количества ключей')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(2)
    plt.plot(x_fit, y_fit2, color="red", label=f"Регрессионный полином {equation2}", linestyle=':')
    plt.step(n, h_avl, label='AVL (Зависимость высоты от ключей)', color='green', where='post')
    plt.step(n, np.log2(n), label='Зависимость h = log(n)', color='blue', linestyle='--', where='post')
    plt.xlabel('Количество ключей')
    plt.ylabel('Высота дерева')
    plt.title('Зависимость высоты AVL-дерева от количества ключей')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(3)
    plt.plot(x_fit, y_fit3, color="red", label=f"Регрессионный полином {equation3}", linestyle=':')
    plt.step(n, h_rb, label='Красно-черное дерево (Зависимость высоты от ключей)', color='green', where='post')
    plt.step(n, np.log2(n), label='Зависимость h = log(n)', color='blue', linestyle='--', where='post')
    plt.xlabel('Количество ключей')
    plt.ylabel('Высота дерева')
    plt.title('Зависимость высоты Красно-черного дерева от количества ключей')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    find_tree_dependence()

    # Binary Search Tree
    print("Binary Search Tree")
    bst = BinarySearchTree()
    for i in range(10):
        bst.insert(random.randint(1, 100))
    bst.print_tree(bst.root)
    print("Pre-order Traversal:")
    pre_order(bst.root)
    print("\nIn-order Traversal:")
    in_order(bst.root)
    print("\nPost-order Traversal:")
    post_order(bst.root)
    print("\nLevel-order Traversal:")
    level_order(bst.root)
    print("\n" + "="*50)

    # AVL Tree
    print("AVL Tree")
    avl = AVLTree()
    for i in range(10):
        avl.insert_key(random.randint(1, 100))
    avl.print_tree(avl.root)
    print("Pre-order Traversal:")
    pre_order(avl.root)
    print("\nIn-order Traversal:")
    in_order(avl.root)
    print("\nPost-order Traversal:")
    post_order(avl.root)
    print("\nLevel-order Traversal:")
    level_order(avl.root)
    print("\n" + "="*50)

    # Red-Black Tree
    print("Red-Black Tree")
    rbt = RedBlackTree()
    for i in range(10):
        rbt.insert(random.randint(1, 100))
    rbt.print_tree(rbt.root)
    print("Pre-order Traversal:")
    pre_order(rbt.root)
    print("\nIn-order Traversal:")
    in_order(rbt.root)
    print("\nPost-order Traversal:")
    post_order(rbt.root)
    print("\nLevel-order Traversal:")
    level_order(rbt.root)
