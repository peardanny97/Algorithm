import time

input = open('input.txt', 'r')
i_lines = input.readlines()
output = open('output.txt', 'r')
o_lines = output.readlines()

s = set(i_lines)
start = time.time()
result = [x for x in o_lines if x not in s]  # to make rsult only list

A = [0 for i in range(10000)]  # for checking
print()
operation = []
key = []
for line in i_lines:
    l = line.split(" ")  # split line with blank
    operation.append(l[0])
    key.append(int(l[1]))
check = open('checker.txt', 'w')

i = 0
check_result = True
for op in operation:
    if op == "I":
        if A[key[i]] == 1:
            if int(result[i]) != 0:
                check.write("Insertion of key {0} is wrong! It should be {1}\n".format(key[i], 0))
                check_result = False
        else:
            A[key[i]] = 1
            if int(result[i]) != key[i]:
                check.write("Insertion of key {0} is wrong! It should be {1}\n".format(key[i], key[i]))
                check_result = False
    elif op == "D":
        if A[key[i]] == 1:
            if int(result[i]) != key[i]:
                check.write("Deletion of key {0} is wrong! It should be {1}\n".format(key[i], key[i]))
                check_result = False
            A[key[i]] = 0
        else:
            if int(result[i]) != 0:
                check.write("Deletion of key {0} is wrong! It should be {1}\n".format(key[i], 0))
                check_result = False
    elif op == "S":
        cnt = 0
        for j in range(1, 10000):
            if A[j] == 1:
                cnt += 1
                if cnt == int(key[i]) and j != int(result[i]):  # if jth smallest item is different from result
                    check.write("Selection of key {0} is wrong! It should be {1}\n".format(key[i], j))
                    check_result = False
                elif cnt == int(key[i]) and j == int(result[i]):
                    break
        if cnt < int(key[i]):
            if int(result[i]) != 0:
                check.write("Selection of key {0} is wrong! It should be {1}\n".format(key[i], 0))
                check_result = False
    elif op == "R":
        cnt = 0
        if A[key[i]] == 0 and int(result[i]) == 0:
            i += 1
            continue
        elif A[key[i]] == 0 and int(result[i]) != 0:
            check.write("Rank of key {0} is wrong! It should be {1}\n".format(key[i], 0))
            check_result = False
            i += 1
            continue

        for j in range(1, int(key[i]) + 1):
            if A[j] == 1:
                cnt += 1
        if cnt != int(result[i]):
            check.write("Selection of key {0} is wrong! It should be {1}\n".format(key[i], cnt))
            check_result = False
    i += 1
end = time.time()
t = (end-start)*1000000
if check_result:
    check.write("Result is correct\n")
    check.write(str(t)+"us")

