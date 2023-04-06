import os
import pandas as pd

list_num = [100, 300, 500, 700, 1000, 1200, 15000, 1700, 2000, 2500, 3000, 5000]

#list_num = [6, 9]

cur_dir = os.getcwd() 
mat_time = 0
arr_time = 0
list_time = 0
mat_times = []
arr_times = []
list_times = []
list_size = []
list_edge = []
for i in list_num:  # for check size
    for j in range(0, 10):
        print("{} argument: {} /10 \n".format(i, j+1))

        os.system(os.path.join('python generator.py') + \
                  ' --size {}'.format(i) + \
                  ' --type 1'
                  )
        os.system(os.path.join('python hw3.py ./input.txt ./output_mat.txt adj_mat'))
        os.system(os.path.join('python hw3.py ./input.txt ./output_list.txt adj_list'))
        os.system(os.path.join('python hw3.py ./input.txt ./output_arr.txt adj_arr'))

        mat_txt = open('output_mat.txt', 'r')
        mat_lines = mat_txt.readlines()
        m_l = mat_lines[-1].strip()
        mat_time += float(m_l.strip("us"))
        list_txt = open('output_list.txt', 'r')
        list_lines = list_txt.readlines()
        l_l = list_lines[-1].strip()
        list_time += float(l_l.strip("us"))
        arr_txt = open('output_arr.txt', 'r')
        arr_lines = arr_txt.readlines()
        a_l = arr_lines[-1].strip()
        arr_time += float(a_l.strip("us"))
        if j == 9:
            list_size.append(i)
            mat_times.append(mat_time/10)
            list_times.append(list_time/10)
            arr_times.append(arr_time/10)
            mat_time = 0
            list_time = 0
            arr_time = 0

result = [list_size, mat_times, list_times, arr_times]
df = pd.DataFrame(result)
df = df.transpose()
df.to_csv('result.csv', header=False, index=False)

edge_list = [1, 5, 10, 20, 50, 100, 150, 200, 250, 300, 350, 400, 450, 499]
for l in edge_list:
    for k in range(0, 10):
        print("edge {}: {} /10 \n".format(l, k + 1))
        os.system(os.path.join('python generator.py') + \
                  ' --size 500' + \
                  ' --type 1'+ \
                  ' --edge {}'.format(l)
                  )
        os.system(os.path.join('python hw3.py ./input.txt ./output_mat.txt adj_mat'))
        os.system(os.path.join('python hw3.py ./input.txt ./output_list.txt adj_list'))
        os.system(os.path.join('python hw3.py ./input.txt ./output_arr.txt adj_arr'))
        mat_txt = open('output_mat.txt', 'r')
        mat_lines = mat_txt.readlines()
        m_l = mat_lines[-1].strip()
        mat_time += float(m_l.strip("us"))
        list_txt = open('output_list.txt', 'r')
        list_lines = list_txt.readlines()
        l_l = list_lines[-1].strip()
        list_time += float(l_l.strip("us"))
        arr_txt = open('output_arr.txt', 'r')
        arr_lines = arr_txt.readlines()
        a_l = arr_lines[-1].strip()
        arr_time += float(a_l.strip("us"))
        if k == 9:
            list_edge.append(l)
            mat_times.append(mat_time / 10)
            list_times.append(list_time / 10)
            arr_times.append(arr_time / 10)
            mat_time = 0
            list_time = 0
            arr_time = 0
result = [list_size, mat_times, list_times, arr_times]
df = pd.DataFrame(result)
df = df.transpose()
df.to_csv('result_type.csv', header=False, index=False)
