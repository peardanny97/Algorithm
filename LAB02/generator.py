import random
import argparse


input = open('input.txt', 'w')
parser = argparse.ArgumentParser(description= 'random_input_generator')
parser.add_argument('--size', type=int, default=1, help='size of list')  # get size of list
args = parser.parse_args()

n = args.size

for i in range(1,n):
    a = str(random.randint(1, 9999))
    op = random.choice(operation)
    input.write(op + " " + a + "\n")
