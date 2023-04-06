# LAB 01

## Code

### Environment
Python 3.9.1 환경에서 구현 아울러 make_csv.py 파일을 실행하기 위해서는 pip install pandas 필요 맥북의 리눅스 터미널에서 실행하였으며, 윈도우에서도 실행되는 것을 확인함

### generator.py
size와 range를 args로 받아 range 내의 정수를 size 개수만큼 만들어주는 파일, 만들어진 list는 input.txt에 첫번째 줄에 size 개수, 두번째 줄의 random 생성된 정수(sliced by whitespace) 세번째 줄에 size 개수 내에서 random 생성된 target으로 저장된다.
(ex: generator.py --size 20 --range 10 , 를 실행하면 20개의 크기를 가진 0부터 9까지의 정수로 만들어 줌)

### checker.py
input.txt로부터 size와 target, list를 입력받고, random.txt와 deter.txt로부터 select한 결과를 입력 받는다. 이를 size 개수만큼 for문을 돌아 만약 list내에 random, deter로부터 select한 결과보다 작은 값이 있으면 a, c를 같은 값이 있으면 b, d를 증가시킨다. 만약 target 값이 a보다 크고 a+b이하라면 random select가 제대로 이루어진 것이며 c보다 크고 c+d 이하라면 deterministic select가 제대로 이루어진 것이다. 만약 결과가 참이라면 checker.txt 에 random/deterministic_selection is correct! 가 첫번째, 두번째 줄에 저장되며 거짓이라면 random/deterministic_selection is not correct! 가 저장된다. 마지막으로 time.time() 함수를 통해 checker.py의 구동 시간을 checker.txt의 세번째 줄에 저장한다.

### random/deterministic_select.py
알고리즘의 구현은 CLRS 교재의 pseudo code와 동일하게 구현하였으며, time.time() 함수를 통해 각각의 구동 시간을 random.txt deter.txt의 두번째 줄에 저장하며, 첫번째 줄에는 select 결과값을 저장하도록 하였다.

### make_csv.py
해당 코드들을 터미널에서 반복적으로 실행시키는 파일. [1, 5, 10, 50, 70, 100, 200, 300, 400, 500, 600, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 9000, 10000, 15000, 17000, 20000, 25000, 27000, 30000, 32000, 35000, 37000, 40000, 42000, 45000, 47000, 50000, 55000, 60000, 65000, 70000, 75000, 80000 , 85000, 90000, 95000, 100000]개의 size list를 generator.py 의 args로 입력시키며, range는 size 개수 범위에 따라 임의의 숫자를 지정하였다. 해당 파일을 실행시키면, 위의 size list의 각각의 size에 대해 10번씩 generator_py, random_select.py, deterministc_select.py, checker.py 가 실행되며 각각의 실행 시간의 평균을 result.csv에 저장하도록 하였다. 



## Time usage

### Checker
![image](https://user-images.githubusercontent.com/37990408/230296944-07e2c7c7-df91-422c-856c-b87d9477a62a.png)
<br>Graph 1. Time usage of checker program

위의 그래프에서 확인할 수 있듯, checker 프로그램에서의 time usage는 O(n)을 나타내는 것을 알 수 있다. 

### Randomized Select vs Deterministic Select 
![image](https://user-images.githubusercontent.com/37990408/230297331-137c2e53-7c08-40cd-93aa-0ad6f94e83e0.png)
<br>Graph 2. Time usage of deterministic & randomized select

위의 그래프에서 확인할 수 있듯, randomized select, deterministic select 모두 O(n)의 시간 복잡도를 갖는 것을 확인할 수 있다. Asymptotic time complexity의 hidden constant ratio를 비교해 보면 Deterministic / Randomized= 1.5384/0.3068 ≈0.0547 로 deterministic select가 6.33배 느린 것을 확인할 수 있다. 이에 대한 원인으로는 deterministic select를 실행할 때에 median of median을 찾는 과정의 시간 복잡도가 O(n)이며 결국 큰 수에 관해서는 randomized select와 차이가 없는 pivot을 찾게 되기 때문이라고 생각할 수 있다.

