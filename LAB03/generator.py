import argparse
import random

parser = argparse.ArgumentParser(description='random_input_generator')
parser.add_argument('--size', type=int, default=10, help='size of graph')  # get size of list
parser.add_argument('--type', type=int, default=1, help='0 for customize 1 for normal')  # get size of list
parser.add_argument('--edge', type=int, default=0, help='0 for type 0, choose edge for each vertex')
args = parser.parse_args()

n = args.size  # size of graph
input_file = open('input.txt', 'w')  # write result at input.txt
input_file.write("{}\n".format(n))

for i in range(1, n+1):
    num_list = list(range(1, n+1))
    num_list.remove(i)  # remove i from num_list, no vertex, i to i is not concerned
    if args.type == 0:  # choose vertex
        m = args.edge
        input_file.write("{} ".format(m))  # num of edges 0 to n/4
        for k in range(m):
            rand_v = random.choice(num_list)
            num_list.remove(rand_v)
            if k != m - 1:
                input_file.write("{} ".format(rand_v))
            elif i == n:
                input_file.write("{}".format(rand_v))
            else:
                input_file.write("{}\n".format(rand_v))

    elif args.type == 1:  # sparse
        m = random.randrange(0, n)
        if m == 0:
            if i == n:
                input_file.write("0")
            else:
                input_file.write("0\n")
        else:
            input_file.write("{} ".format(m))  # num of edges 0 to n/4
            for k in range(m):
                rand_v = random.choice(num_list)
                num_list.remove(rand_v)
                if k != m-1:
                    input_file.write("{} ".format(rand_v))
                elif i == n:
                    input_file.write("{}".format(rand_v))
                else:
                    input_file.write("{}\n".format(rand_v))
    # else:  # sparse
    #     m = random.randrange(int(2/3*n), n)
    #     if m == 0:
    #         if i == n:
    #             input_file.write("0")
    #         else:
    #             input_file.write("0\n")
    #     else:
    #         input_file.write("{} ".format(m))  # num of edges 0 to n/4
    #         for k in range(m):
    #             rand_v = random.choice(num_list)
    #             num_list.remove(rand_v)
    #             if k != m-1:
    #                 input_file.write("{} ".format(rand_v))
    #             elif i == n:
    #                 input_file.write("{}".format(rand_v))
    #             else:
    #                 input_file.write("{}\n".format(rand_v))

