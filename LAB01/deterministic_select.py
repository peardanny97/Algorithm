import random
import time

input_txt = open('input.txt', 'r')  # get input from input.txt
lines = input_txt.readlines()

n = int(lines[0].strip())
list_string = lines[1].strip().split(" ")
list = [int (str)for str in list_string]
target = int(lines[2].strip())


def IS(A):  # Insertion sort
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

    if(len(A)%2 == 0):  # number of A is even
        return A[int(len(A)/2 - 1)]
    else: return A[int(len(A)//2)]


def SearchbyValue(A,n):  #search index by value n
    for i in range(0,len(A)):
        if A[i] == n: return i


def PartitionbyPivot(A, p, r, pivot):
    A[r], A[pivot] = A[pivot], A[r]  # swap pivot, r element
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap i, j element
    A[i+1], A[r] = A[r], A[i+1]  # swap i+1, r element
    return i+1


def Select(A, p, r, i):
    n = r - p + 1   
    M = []  # list of medians
    pivot = p

    if n == 1:
        return A[p]  # list have only one element

    if n % 5 == 0: j = n/5
    else: j = n//5 + 1

    j = int(j)

    for l in range(j):
        if l==j-1:  #last group's element can be smaller than 5
            M.append(IS(A[p + 5*l : r + 1]))
        else:
            M.append(IS (A[p + 5*l: p + 5*l+5]))

    if len(M)%2 == 0 : m = len(M)//2 - 1
    else: m = len(M)//2

    return Select(M, 0, len(M) - 1, m)

def DS(A,p,r,i):
    if p == r: return A[p]
    p_element = Select(A,p,r,i)
    pivot = SearchbyValue(A,p_element)  # index of pivot
    q = PartitionbyPivot(A,p,r,pivot)
    k = q-p+1

    if i == k:  # pivot value is Answer
        return A[q]
    elif i < k:  # key value is at left side of pivot
        return DS(A, p, q-1, i)
    else:
        return DS(A, q+1, r, i-k)  # key value is at right side of pivot



start = time.time()
result = DS(list, 0, n-1, target)
end = time.time()

random_txt = open('deter.txt', 'w')
random_txt.write("{}\n".format(result))
random_txt.write("{}us".format((end-start)*1000000))