import os
import pandas as pd

#list = [5]
list_num = [1, 5, 10, 50, 70, 100, 200, 300, 400, 500, 600, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 9000, 10000, 15000, 17000, 20000,
            25000, 27000, 30000, 32000, 35000, 37000, 40000, 42000, 45000, 47000, 50000, 55000, 60000, 65000, 70000, 75000, 80000
            , 85000, 90000, 95000, 100000]

list_n = []
list_randtime = []
list_detertime = []
list_checkertime = []

cur_dir = os.getcwd() 

for i in list_num:
    for j in range(0,10):
        print("{} list: {} /10 \n".format(i,j+1))

        if j == 0:
            rt = 0
            dt = 0
            ct = 0

        if i <= 100: r = 70
        elif i <= 1000: r = 700
        elif i <= 5000: r = 3000
        elif i <= 300000: r = 20000
        else: r = 70000

        os.system(os.path.join('python generator.py') + \
            ' --size {}'.format(i)  + \
            ' --range {}'.format(r)
                )
        os.system(os.path.join('python randomized_select.py'))
        os.system(os.path.join('python deterministic_select.py'))
        os.system(os.path.join('python checker.py'))
        
        random_txt = open('random.txt', 'r')  
        lines = random_txt.readlines()
        l = lines[1].strip()
        l = l.strip("us")
        rt += float(l)


        deter_txt = open('deter.txt', 'r')  
        lines = deter_txt.readlines()
        l = lines[1].strip()
        l = l.strip("us")
        dt += float(l)

        checker_txt = open('checker.txt', 'r')  
        lines = checker_txt.readlines()
        l = lines[0].strip()
        if "not" in l:
            raise SystemError("not correct you fool")
        l = lines[1].strip()
        if "not" in l:
            raise SystemError("not correct you fool")
        l = lines[2].strip()
        l = l.strip("us")
        ct += float(l)

        if(j == 9):
            list_n.append(i)
            list_checkertime.append(ct/10)
            list_detertime.append(dt/10)
            list_randtime.append(rt/10)


list = [list_n, list_randtime, list_detertime, list_checkertime]
df = pd.DataFrame(list)
df = df.transpose()
df.to_csv('result.csv',header= False, index= False)
