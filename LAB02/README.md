# LAB 02 - Order-Statistic Tree

## Code

###	Environment
Python 3.9.1 환경에서 구현, 아울러 make_csv.py 파일을 실행하기 위해서는 pip install pandas 필요.
맥북의 리눅스 터미널에서 실행하였음, teminal에서 input.txt가 준비되면 python OS.py python checker.py를 순서대로 입력할 경우 output.txt와 checker.txt가 순서대로 저장됨.

### generator.py
size를 args로 받아 size 개수만큼의 argument를 1~9999의 key와 함께 input.txt으로 만들어주는 파일, input.txt의 format은 sample_input.txt와 동일

###	checker.py
input.txt와 output.txt를 입력으로 받는다. 모든 값이 0으로 초기화된 A라는 list를 만든다. 그 후 input.txt와 output.txt에서 중복되는 부분인 input.txt 부분을 output.txt에서 뺀 output result와 input.txt의 input으로부터 opeation과 key라는 리스트를 받는다.
 
각각의 ith operation에서 I(Input)의 경우 A[key]값에 해당 값이 존재(1)하면 result[i]에 0이, 존재하지 않는다면 result[i]에 key값이 있는지 확인 후 A[key] = 1을 할당한다. 
<br>만약 insert return값이 다르다면 check.txt에 적혀야 할 key 값을 작성한 후 check_result값을 false로 변경한다. 
 
유사한 방법으로 D(Deletion)의 경우 A[key]값에 1이 있다면 0으로 수정 후 result값과 비교, 이미 1이 있다면 result[i]에 0이 출력되었는지 확인한다. 
 
S(Selection)의 경우 list A를 A[1]부터 확인해가며 1의 개수를 count한다. 만약 count와 key값이 같을 때의 iterator의 값과 result가 같지 않다면 false를 출력한다. 또한 list를 전부 확인했을 때에 cnt의 개수가 key보다 작을 경우 result에 0이 출력되었는지를 확인한다.
 
마지막으로 R(Rank)의 경우 우선 A[key] 값이 List, 즉 tree에 존재하는지 확인하고 존재하지 않는다면 result에 0이 저장되었는가를 확인한다. 저장되어 있을 경우 A[1]부터 A[key]값까지 1의 개수를 count한 후 그 값이 result[i]와 같은가를 확인한다.
 이렇게 확인한 check_result에서 false로 변하지 않았을 경우 check_result에 “Result is correct”라는 문구와 걸린 시간을 저장한다.
 
각각의 operation이 O(1)의 시간복잡도를 갖고 있는데 이러한 operation을 n번 실행하니 checker의 time complexity는 O(n)일 것이라 예상할 수 있으며 이는 후술할 make_csv를 통해 확인 가능했다.

###	OS.py
Order-statistic tree를 교재의 RB tree pseudo code에 기반하여 작성하였다. 이 때에 OS-Tree의 structure를 유지하기 위하여 size라는 요소를 추가하였으며, insert, delete 등을 진행할 때에 size를 update 하는 과정을 추가하여 RB tree의 구조를 유지하며 각각의 node에 size를 저장하도록 코드를 수정하였다.

###	make_csv.py
해당 코드들을 [1, 5, 10, 50, 70, 100, 200, 300, 400, 500, 600, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 9000, 10000]개의 size list를 generator.py 의 args로 입력시키는 코드이다. 해당 파일을 실행시키면, 위의 size list의 각각의 size에 대해 10번씩 generator.py, OS.py, checker.py 가 실행되며 checker.py의 실행 시간의 평균을 result.csv에 저장하도록 하였다. 



## Time usage

### Checker

 ![image](https://user-images.githubusercontent.com/37990408/230301796-dcb52144-8e66-4679-8f11-7da3488a8d80.png)
<br>Graph 1. Time usage of checker program

위의 그래프에서 확인할 수 있듯, 1-2에서 예상한 것과 같이 checker 프로그램에서의 time usage는 O(n)을 나타내는 것을 알 수 있다. 

