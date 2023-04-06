import random
import time

input_txt = open('input.txt', 'r')  # get input from input.txt
lines = input_txt.readlines()

n = int(lines[0].strip())
list_string = lines[1].strip().split(" ")
list = [int (str)for str in list_string]
target = int(lines[2].strip())


def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap i, j element
    A[i+1], A[r] = A[r], A[i+1]  # swap i+1, r element
    return i+1


def RP(A, p, r):
    i = random.randrange(p, r)  # choose random pivot
    A[r], A[i] = A[i], A[r]  # swap r, i element
    return Partition(A, p, r)


def RS(A, p, r, i):  # Randomized Selection
    if p == r:  # A has only one value
        return A[p]
    q = RP(A, p, r)  # use Randomized Partition
    k = q-p+1
    if i == k:  # pivot value is Answer
        return A[q]
    elif i < k:  # key value is at left side of pivot
        return RS(A, p, q-1, i)
    else:
        return RS(A, q+1, r, i-k)  # key value is at right side of pivot


start = time.time()
result = RS(list, 0, n-1, target)
end = time.time()

random_txt = open('random.txt', 'w')
random_txt.write("{}\n".format(result))
random_txt.write("{}us".format((end-start)*1000000))