import time

input_txt = open('input.txt', 'r')  # get input from input.txt
lines = input_txt.readlines()

n = int(lines[0].strip())
list_string = lines[1].strip().split(" ")
list = [int(str)for str in list_string]
target = int(lines[2].strip())

random_txt = open('random.txt', 'r')  # get result from random.txt
random_lines = random_txt.readlines()
random_result = int(random_lines[0].strip())

deter_txt = open('deter.txt', 'r')  # get result from random.txt
deter_lines = deter_txt.readlines()
deter_result = int(deter_lines[0].strip())

# random selection
start = time.time()
a = 0
b = 0
for i in range(n):
    if (list[i] < random_result):
        a += 1  # if number in result is smaller than result
    elif (list[i] == random_result):
        b += 1  # if number in result is smaller than result


c = 0
d = 0
for i in range(n):
    if (list[i] < deter_result):
        c += 1  # if number in result is smaller than result
    elif (list[i] == deter_result):
        d += 1  # if number in result is smaller than result


end = time.time()

checker_txt = open('checker.txt', 'w')  # write result at checker.txt



if target == 1 and a == 0:
    checker_txt.write("random_selection result is correct!\n")
elif a < target <= a+b:
    checker_txt.write("random_selection result is correct!\n")
else:
    checker_txt.write("random_selection result is not correct!\n")


if target == 1 and c == 0:
    checker_txt.write("deterministic_selection result is correct!\n")
elif c < target <= c+d:
    checker_txt.write("deterministic_selection result is correct!\n")
else:
    checker_txt.write("deterministic_selection result is not correct!\n")


checker_txt.write("{}us".format((end-start)*1000000))