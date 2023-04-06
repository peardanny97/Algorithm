import random
import argparse

parser = argparse.ArgumentParser(description='random_input_generator')
parser.add_argument('--size', type=int, default=1, help='size of list')  # get size of list
parser.add_argument('--range', type=int, default=200, help='size of list')  # get size of list
args = parser.parse_args()

n = args.size  # size of list
i = random.randint(1, n)  # choose random ith smallest object


result = open('input.txt', 'w')  # write result at input.txt

result.write("{}\n ".format(n))
for j in range(n):
    result.write("{} ".format(random.randint(0, args.range)))  # choose number from 0 to 
result.write("\n")
result.write("{}".format(i))
