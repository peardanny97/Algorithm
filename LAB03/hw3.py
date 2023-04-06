import sys
import time
sys.setrecursionlimit(10**7)

class matGraph:
    def __init__(self, size):
        self.adjMatrix = []
        if size <= 0:
            print("size has to be bigger than 0")
        else:
            self.connected = []; self.result = []; self.color = []; self.f = []
            self.n = 1  # to compute last vertex
            self.size = size
            for i in range(size+1):  # make size*size matrix with 0, we'll ignore row 0 col 0
                self.adjMatrix.append([0 for j in range(size+1)])
                self.color.append("WHITE")
                self.f.append(0)

    def add_edge(self, start, end):
        self.adjMatrix[start][end] = 1

    def DFS_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.adjMatrix[i][j] == 1:  # if adj is not visited
                self.DFS_visit(j)
        self.color[i] = "BLACK"
        self.f[self.n] = i  # nth finished vertex is i
        self.n += 1

    def DFS(self):
        self.n = 1  # initialize n
        for i in range(size+1):
            self.color[i] = "WHITE"
        for i in range(1, size+1):  # we'll ignore 0
            if self.color[i] == "WHITE":
                self.DFS_visit(i)

    def DFS_T_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        self.connected.append(i)
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.adjMatrix[j][i] == 1:  # if adj(reversed) is not visited
                self.DFS_T_visit(j)
        self.color[i] = "BLACK"

    def DFS_T(self):
        for i in range(size + 1):
            self.color[i] = "WHITE"
        for i in range(size, 0, -1):  # in decreasing order
            self.connected = []
            if self.color[self.f[i]] == "WHITE":
                self.DFS_T_visit(self.f[i])
            if len(self.connected) >= 1:  # we need to sort strongly connected components
                self.connected.sort()
                str_c = [str(x) for x in self.connected]
                self.result.append(str_c)

    def print_mat(self):
        print(self.adjMatrix)


class Node:  # node for adjacency list
    def __init__(self, v):
        self.vertex = v
        self.next = None


class listGraph:
    def __init__(self, size):
        if size <= 0:
            print("size has to be bigger than 0")
        else:
            self.connected = []; self.result = []; self.color = []; self.f = []
            self.n = 1  # to compute last vertex
            self.size = size
            self.adjList = [None] * (self.size + 1)  # we'll ignore vertex 0
            self.adjList_T = [None] * (self.size + 1)  # make transpose of adj list
            for i in range(size+1):
                self.color.append("WHITE")
                self.f.append(0)

    def add_T_edge(self, start, end):
        node = Node(end)
        node.next = self.adjList_T[start]
        self.adjList_T[start] = node

    def add_edge(self, start, end):
        node = Node(end)
        node.next = self.adjList[start]
        self.adjList[start] = node

    def isConnected(self, list, start, end):  # check if start & end point is connected
        if list[start] is None:
            return False
        else:
            if list[start].vertex == end:
                return True
            else:
                next_v = list[start].next
                while next_v is not None:
                    if next_v.vertex == end:
                        return True
                    next_v = next_v.next
                return False

    def DFS_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.isConnected(self.adjList, i, j):  # if adj is not visited
                self.DFS_visit(j)
        self.color[i] = "BLACK"
        self.f[self.n] = i  # nth finished vertex is i
        self.n += 1

    def DFS(self):
        self.n = 1  # initialize n
        for i in range(size+1):
            self.color[i] = "WHITE"
        for i in range(1, size+1):  # we'll ignore 0
            if self.color[i] == "WHITE":
                self.DFS_visit(i)

    def DFS_T_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        self.connected.append(i)
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.isConnected(self.adjList_T, i, j):  # if adj(reversed) is not visited
                self.DFS_T_visit(j)
        self.color[i] = "BLACK"

    def DFS_T(self):
        for i in range(size + 1):
            self.color[i] = "WHITE"
        for i in range(size, 0, -1):  # in decreasing order
            self.connected = []
            if self.color[self.f[i]] == "WHITE":
                self.DFS_T_visit(self.f[i])
            if len(self.connected) >= 1:  # we need to sort strongly connected components
                self.connected.sort()
                str_c = [str(x) for x in self.connected]
                self.result.append(str_c)


class arrGraph:
    def __init__(self, size, v_size):
        if size <= 0:
            print("size has to be bigger than 0")
        else:
            self.size = size
            self.vertex_list = [0, ]; self.vertex_list_T = [0,]
            # start with zero for preventing confusion of size 0 & make initial size 0
            self.edge_list = []; self.edge_list_T = []
            self.connected = []; self.result = []; self.color = []; self.f = []
            self.n = 1  # to compute last vertex
            for i in v_size:
                self.vertex_list.append(i)
                self.vertex_list_T.append(0)
            for i in range(size+1):
                self.color.append("WHITE")
                self.f.append(0)

    def add_edge(self, end):
        self.edge_list.append(end)

    def transposeArr(self):
        for edge in self.edge_list:
            self.vertex_list_T[edge] += 1  # make reversed vertex list
        v = 0
        for i in range(1, size+1):
            v += self.vertex_list_T[i]
            self.vertex_list_T[i] = v
        for i in range(1, size+1):  # make reversed edge list this will take O(V^2) time
            for j in range(1, size+1):
                if self.isConnected(self.vertex_list,self.edge_list, j, i):
                    self.edge_list_T.append(j)

    def isConnected(self, vertex_list, edge_list, start, end):  # check if start & end is connected
        if vertex_list[start] == 0 or vertex_list[start-1] == vertex_list[start]:
            # if vertex_list has 0 vertex
            return False
        else:
            for i in range(vertex_list[start-1], vertex_list[start]):
                if edge_list[i] == end:
                    return True
            return False

    def DFS_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.isConnected(self.vertex_list, self.edge_list, i, j):  # if adj is not visited
                self.DFS_visit(j)
        self.color[i] = "BLACK"
        self.f[self.n] = i  # nth finished vertex is i
        self.n += 1

    def DFS(self):
        self.n = 1  # initialize n
        for i in range(size+1):
            self.color[i] = "WHITE"
        for i in range(1, size+1):  # we'll ignore 0
            if self.color[i] == "WHITE":
                self.DFS_visit(i)

    def DFS_T_visit(self, i):
        self.color[i] = "GRAY"  # white vertex has been visited
        self.connected.append(i)
        for j in range(1, size+1):
            if self.color[j] == "WHITE" and self.isConnected(self.vertex_list_T, self.edge_list_T, i, j):  # if adj(reversed) is not visited
                self.DFS_T_visit(j)
        self.color[i] = "BLACK"

    def DFS_T(self):
        for i in range(size + 1):
            self.color[i] = "WHITE"
        for i in range(size, 0, -1):  # in decreasing order
            self.connected = []
            if self.color[self.f[i]] == "WHITE":
                self.DFS_T_visit(self.f[i])
            if len(self.connected) >= 1:  # sort strongly connected components
                self.connected.sort()
                str_c = [str(x) for x in self.connected]  # save as str for lexicographical order
                self.result.append(str_c)


fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

i_lines = fin.readlines()
i_l = 0; size = 0; edge_list = []; vertex_size = []

for line in i_lines:
    l = line.strip()
    l = l.split(" ")  # split line with blank
    if i_l == 0:
        size = int(l[0])
    else:
        j_l = 0
        for a in l:
            if j_l == 0:
                vertex_size.append(int(a))
            else:
                edge_list.append([i_l, int(a)])
            j_l += 1
    i_l += 1

if sys.argv[3] == "adj_mat":
    adj_mat = matGraph(size)
    for E in edge_list:
        adj_mat.add_edge(E[0], E[1])
    start = time.time()
    adj_mat.DFS()
    adj_mat.DFS_T()
    result = sorted(adj_mat.result)
    end = time.time()
    t = (end - start) * 1000000
    for o_line in result:
        for o in o_line:
            fout.write(o)
            if o != o_line[-1]:
                fout.write(" ")
            else:
                fout.write("\n")
    fout.write(str(t) + "us")

elif sys.argv[3] == "adj_list":
    adj_list = listGraph(size)
    for E in edge_list:
        adj_list.add_edge(E[0], E[1])
    adj_list.DFS()
    start = time.time()
    for E in edge_list:
        adj_list.add_T_edge(E[1], E[0])
    adj_list.DFS_T()
    result = sorted(adj_list.result)
    end = time.time()
    t = (end - start) * 1000000
    for o_line in result:
        for o in o_line:
            fout.write(o)
            if o != o_line[-1]:
                fout.write(" ")
            else:
                fout.write("\n")
    fout.write(str(t) + "us")

elif sys.argv[3] == "adj_arr":
    v = 0
    v_size = []
    for i_v in vertex_size:
        v = v + i_v
        v_size.append(v)
    adj_arr = arrGraph(size, v_size)
    for E in edge_list:
        adj_arr.add_edge(E[1])
    start = time.time()
    adj_arr.DFS()
    adj_arr.transposeArr()
    adj_arr.DFS_T()
    result = sorted(adj_arr.result)
    end = time.time()
    t = (end - start) * 1000000
    for o_line in result:
        for o in o_line:
            fout.write(o)
            if o != o_line[-1]:
                fout.write(" ")
            else:
                fout.write("\n")
    fout.write(str(t) + "us")