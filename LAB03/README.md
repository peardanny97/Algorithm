# LAB 03 - Directed Graph

## Code

### Environment
Python 3.9.1 환경에서 구현, 아울러 make_csv.py 파일을 실행하기 위해서는 pip install pandas 필요, 데스크탑의 VScode에서 실행

### generator.py
size를 args로 받아 size 개수만큼의 graph를 생성, 만약 type1일 경우에는 각 vertex에 랜덤한 개수의 edge를, type 0의 경우 각 vertex에 입력받은 edge 개수만큼의 edge를 생성함

### hw3.py
argument로 adj_mat, adj_list, adj_arr를 받음에 따라 각각의 adjacency data struct에 따라 strongly connected components를 출력하는 코드, 알고리즘의 경우 교과서의 617쪽의 STRONGLY-CONNECTED-COMPONENTS(G) 에 따라 코드를 작성하였다. 혼돈을 방지하기 위해 각각의 adj_list, mat, arr의 index가 0 인 경우에는 생략하고 코드를 작성하였다. Adj_mat의 경우 [size+1][size+1]의 matrix를 만들어 0행과 0열은 무시하고 알고리즘에 따라 코드를 작성, 이 때 reversed graph의 경우 행렬의 열과 행을 뒤바꾸어 만들었다. Adj_list의 경우 list structure를 만들기 위해 node를 define한 후 각각의 node를 link하여 linked list 형태로 작성, 이 때 reversed graph는 graph를 처음 만들 때와 동일한 방식으로 만들었으며, 편의를 위해 isConnected라는 함수를 통해 list를 제공받았을 때에 start와 end의 연결성을 확인하도록 함. Adj_arr도 list와 유사한 방식으로 작성되었으며, transpose의 경우 모든 vertex에 대해 isConnected를 확인하는 방식으로 만들었기에 Θ(V^2 )의 시간이 걸리도록 만들어졌음

### make_csv.py

해당 코드들을 두 가지 형태로 분석하기 위한 코드. 우선 각각의 size가 미치는 time usage를 확인하기 위해 [100, 300, 500, 700, 1000, 1200, 1500, 1700, 2000]의 크기를 generator.py에 assign하여 adj_mat, adj_list, adj_arr의 time usage를 csv 형태로 저장함, 이 때, 각각의 graph의 경우 0~V-1 사이의 edge를 random하게 vertex가 갖도록 하였음. 두번째로는 graph의 density가 미치는 영향을 확인하기 위해 vertex가 500인 graph에 대해 각각의 V에 대해 [1, 5, 10, 20, 50, 100, 150, 200, 250, 300, 350, 400, 450, 499]개의 edge를 만들도록 한 뒤 각각의 data structure에 대한 time usage를 csv에 저장하도록 함. 그 결과는 아래와 같음

## Time usage

### size

 ![image](https://user-images.githubusercontent.com/37990408/230303448-209ae294-d02a-4e2c-ae28-af2c0952e3e1.png)
Graph 1. Time usage of each structure by size

파이썬의 random 함수를 통하여 edge개수를 결정하였기에 평균적으로 |E|=|V|^1.5의 관계를 만족할 것이다. 이론적인 SCC의 시간복잡도 Θ(|V|+|E|)=Θ(|V|+|V|^1.5 )=Θ(|V|^1.5 )인데 반해 adj_arr의 경우 Θ(|V|^2 )의 형태를 갖는 것을 확인 가능하다. 이는 앞서 언급한 코드에서 transpose의 과정이 Θ(|V|^2 )이기에 발생하는 현상이다. 또한 adj_mat가 다른 두 data structure에 비해 낮은 time usage를 보이는데, 이는 adj_mat에서는 transpose위한 과정이 행과 열을 바꿔 입력하는 것으로 대체되었으며, isConnected 함수 또한 필요하지 않았기에 다른 두 함수에 비해 O(E)=O(V^1.5 )의 과정이 적어 일어나는 일이라 예측할 수 있다. 즉 adj_mat의 경우 time usage는 확연하게 적고 반대로 큰 space usage임을 알 수 있다.

### Density

![image](https://user-images.githubusercontent.com/37990408/230304015-fe789741-fbe3-4878-9be5-5ee3813e6a7c.png)
<br>Graph 2. Time usage of each structure by density

정점의 개수가 500일 때 edge가 1~499일 때의 time usage 그래프는 다음과 같다. adj_mat의 경우 edge와 시간에 따른 변화가 거의 없는 반면, adj_arr, adj_list의 경우 density가 증가함에 따라 시간복잡도가 증가하는 것을 알 수 있다. 이는 density가 증가함에 따라 isConnected함수의 depth가 증가하기 때문에 일어나는 일임을 알 수 있고, adj_arr의 time usage가 더 큰 것은 transpose의 영향이 크다는 것을 알 수 있다. 


## Conclusion
  SCC의 time usage만을 고려했을 때에는 adj_mat를 사용하는 것이 가장 이상적이지만, 이번 과제에서는 실제 해당 graph를 만들기 위해 structure를 만드는 시간을 포함하지 않고 있다. Adj_mat의 경우 행렬을 만드는 데에만 Θ(|V^2 |) 의 시간이 소모되며, space usage 또한 다른 structure에 비해 훨씬 크다는 것을 알 수 있다. 즉, 이미 만들어진 graph에 대해서 SCC를 구할 때에는 adj_matrix가 가장 이상적이지만, 다른 요소들을 고려할 경우에는 선호되는 자료구조가 다를 수 있다는 것을 알 수 있다. 
