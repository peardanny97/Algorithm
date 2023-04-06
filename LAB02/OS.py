import sys
sys.setrecursionlimit(10**7)


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.color = "RED"
        self.size = 0
        self.rank = 0


class OSTree:
    def __init__(self):
        self.NIL = Node("NIL")  # first make node NIL
        self.NIL.color = "BLACK"
        self.T = self.NIL  # if there is no node, root points to NIL node

    def treeSearch(self, t, x):
        if t == self.NIL or t.key == x:
            return t
        if x < t.key:
            return self.treeSearch(t.left, x)
        else:
            return self.treeSearch(t.right, x)

    def insert(self, key):
        if self.NIL != self.treeSearch(self.T, key): return 0  # if key already exists in tree return 0

        y = self.NIL  # NIL node
        x = self.T  # root of tree
        z = Node(key)  # node with element key
        z.size = 1
        while x != self.NIL:  # size of node has to be incremented while finding node's position
            y = x
            y.size += 1  # increment size of node
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NIL:
            self.T = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = "RED"
        self.insertFixup(z)  # needs fixup to satisfy RBtree structure
        return key

    def leftRotate(self, x):
        y = x.right
        x.right = y.left  # turn y's left subtree into x's right subtree
        if y.left != self.NIL: y.left.p = x
        y.p = x.p  # link x's parent to y
        if x.p == self.NIL:
            self.T = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x  # put x on y's left
        x.p = y
        y.size = x.size  # size has to be changed
        x.size = x.left.size + x.right.size + 1

    def rightRotate(self, x):
        y = x.left
        x.left = y.right  # turn y's right subtree into x's left subtree
        if y.right != self.NIL: y.right.p = x
        y.p = x.p  # link x's parent to y
        if x.p == self.NIL:
            self.T = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x  # put x on y's right
        x.p = y
        y.size = x.size  # size has to be changed
        x.size = x.left.size + x.right.size + 1

    def insertFixup(self, z):
        while z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "RED":
                    z.p.color = "BLACK"  # case 1
                    y.color = "BLACK"  # case 2
                    z.p.p.color = "RED"  # case 1
                    z = z.p.p  # case 1
                else:
                    if z == z.p.right:
                        z = z.p  # case 2
                        self.leftRotate(z)  # case 2
                    z.p.color = "BLACK"  # case 3
                    z.p.p.color = "RED"  # case 3
                    self.rightRotate(z.p.p)  # case 3
            else:  # right & left exchanged
                y = z.p.p.left
                if y.color == "RED":
                    z.p.color = "BLACK"  # case 1
                    y.color = "BLACK"  # case 2
                    z.p.p.color = "RED"  # case 1
                    z = z.p.p  # case 1
                else:
                    if z == z.p.left:
                        z = z.p  # case 2
                        self.rightRotate(z)  # case 2
                    z.p.color = "BLACK"  # case 3
                    z.p.p.color = "RED"  # case 3
                    self.leftRotate(z.p.p)  # case 3
        self.T.color = "BLACK"

    def delete(self, key):
        z = self.treeSearch(self.T, key)  # find node where key exists
        if z == self.NIL: return 0  # if key does not exists in tree return 0

        y = z
        y_original = y.color
        if z.left == self.NIL:  # z has only right child or leaf
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:  # z has only left child or leaf
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            y_original = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        if y_original == "BLACK":
            self.deleteFixup(x)

        w = x.p  # to reduce size of x's parents
        while w != self.NIL:  # update size from x's p to root T
            w.size = w.left.size + w.right.size + 1
            w = w.p

        return key

    def transplant(self, u, v):  # transplant v to u
        if u.p == self.NIL:
            self.T = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def treeMinimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def deleteFixup(self, x):
        while x != self.T and x.color == "BLACK":
            if x == x.p.left:
                w = x.p.right
                if w.color == "RED":
                    w.color = "BLACK"  # case 1
                    x.p.color = "RED"  # case 1
                    self.leftRotate(x.p)  # case 1
                    w = x.p.right  # case 1
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"  # case 2
                    x = x.p  # case 2
                else:
                    if w.right.color == "BLACK":  # case 3
                        w.left.color = "BLACK"  # case 3
                        w.color = "RED"  # case 3
                        self.rightRotate(w)  # case 3
                        w = x.p.right  # case 3
                    w.color = x.p.color  # case 4
                    x.p.color = "BLACK"  # case 4
                    w.right.color = "BLACK"  # case 4
                    self.leftRotate(x.p)  # case 4
                    x = self.T  # case 4
            else:  # exchange left and right
                w = x.p.left
                if w.color == "RED":
                    w.color = "BLACK"  # case 1
                    x.p.color = "RED"  # case 1
                    self.rightRotate(x.p)  # case 1
                    w = x.p.left  # case 1
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"  # case 2
                    x = x.p  # case 2
                else:
                    if w.left.color == "BLACK":  # case 3
                        w.right.color = "BLACK"  # case 3
                        w.color = "RED"  # case 3
                        self.leftRotate(w)  # case 3
                        w = x.p.left  # case 3
                    w.color = x.p.color  # case 4
                    x.p.color = "BLACK"  # case 4
                    w.left.color = "BLACK"  # case 4
                    self.rightRotate(x.p)  # case 4
                    x = self.T  # case 4
        x.color = "BLACK"

    def select(self, x, i):
        if i < 0 or i > self.T.size:
            return 0
        else:
            r = x.left.size + 1
            if i == r: return x.key
            elif i < r: return self.select(x.left, i)
            else: return self.select(x.right, i-r)

    def rank(self, i):
        x = self.treeSearch(self.T, i)
        if x == self.NIL: return 0
        else:
            r = x.left.size + 1
            y = x
            while y != self.T:
                if y == y.p.right: r = r + y.p.left.size + 1
                y = y.p
            return r


operation = []  # list of operation from input
key = []  # number for operation from input
input_txt = open('input.txt', 'r')
lines = input_txt.readlines()

for line in lines:
    l = line.split(" ")  # split line with blank
    operation.append(l[0])
    key.append(int(l[1]))

Tree = OSTree()
result = []
i = 0

for op in operation:
    if op == "I":
        tmp = Tree.insert(key[i])  # if operation is insert
        result.append(tmp)
    elif op == "D":
        tmp = Tree.delete(key[i])  # if operation is delete
        result.append(tmp)
    elif op == "S":
        tmp = Tree.select(Tree.T, key[i])  # if operation is select
        result.append(tmp)
    elif op == "R":
        tmp = Tree.rank(key[i])  # if operation is rank
        result.append(tmp)
    i += 1

output = open('output.txt', 'w')
for l in lines:
    output.write(l)
for r in result:
    output.write(str(r))
    output.write("\n")
