import os
import pandas as pd

list_num = [1, 5, 10, 50, 70, 100, 200, 300, 400, 500, 600, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 9000, 10000]

list_n = []
list_checkertime = []

cur_dir = os.getcwd() 

for i in list_num:
    for j in range(0,10):
        print("{} argument: {} /10 \n".format(i,j+1))

        if j == 0:
            rt = 0
            dt = 0
            ct = 0

        os.system(os.path.join('python generator.py') + \
            ' --size {}'.format(i)
                )
        os.system(os.path.join('python OS.py'))
        os.system(os.path.join('python checker.py'))

        checker_txt = open('checker.txt', 'r')  
        lines = checker_txt.readlines()
        if lines[0].strip() != "Result is correct!":
            raise SystemError("result is not correct")
        l = lines[1].strip()
        l = l.strip("us")
        ct += float(l)

        if(j == 9):
            list_n.append(i)
            list_checkertime.append(ct/10)


list = [list_n, list_checkertime]
df = pd.DataFrame(list)
df = df.transpose()
df.to_csv('result.csv',header= False, index= False)
