# -*- coding: utf-8 -*-


# from math import sqrt


# def F(n):
#     return ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))


# print(F(10))

# def F():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# def SubFib(startNumber, endNumber):
#     for cur in F():
#         if cur > endNumber:
#             return
#         if cur >= startNumber:
#             yield cur


# for i in SubFib(10, 200):
#     print(i)

# length = 'aaa'
# count = 0
# a = 1
# b = 1
# c = a + b

# while len(length) <= 100:
#     a = b
#     b = c
#     c = a + b
#     count = count + 1
#     str1 = str(c)
#     if len(str1) > len(length):
#         length = str1

# if 1 + 1 * 3 == 6:
#     print("Yes")
# else:
#     print("No")
# i = 3
# while i >= 0:
#     print(i)
#     i = i - 1
#     print(i)
# print(1 + 1 * 3)
# print(length)
# print(count)

# x = 0

# while x <= 20:
#     print(x)
#     x += 2


A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
print(A0, A1, A2, A3, A4, A5, A6)


class Node:

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(),
                           self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None

    def preorder(self):
        if self.root is not None:
            print("PreOrder")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()


bst = Tree()
print(bst.insert(10))
print(bst.insert(5))
bst.preorder()
print(bst.getHeight())
bst.postorder()
bst.inorder()
print(bst.remove(10))
bst.preorder()


def func(x):
    res = 0
    for i in range(x):
        res += i
    return res


print(func(4))
