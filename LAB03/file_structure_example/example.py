import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
a, b = map(int, fin.readline().split())
result = 0
if sys.argv[3] == "add":
    result = a + b
elif sys.argv[3] == "sub":
    result = a - b
fout.write(f"{result}\n")