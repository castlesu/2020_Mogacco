# 2020_Mogacco
2020 하계 모각코 팀강서연 - 성수현

## 2020. 07. 01(week1)
paycharm 과 github 연동

## 2020. 07. 08(week2)
DFS/BFS의 내용요약

DFS : Depth First Search (깊이 우선 탐색)

루트 노드(또는 임의의 노드)에서 시작하여 다음분기(branch)로 넘어가기 전에 해당분기를 완벽하게 탐색하는 방식
1. 모든 노드를 방문하고자 할때 
2. BFS보다 간단함
3. BFS보다 느림
4. 스택 또는 재귀함수(보편적)로 구현

![image](https://user-images.githubusercontent.com/26875426/86904852-3c34f400-c14c-11ea-9bf6-9d77b984a978.png)


BFS : Breadth First Search (너비 우선 탐색)

루트 노드(또는 임의의 노드)에서 시작하여 인접한 노드를 먼저 탐색하는 방식

시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법
1. (주로) 두 노드사이의 최단경로를 찾을 때
2. 큐로 구현(FIFO 원칙)


![image](https://user-images.githubusercontent.com/26875426/86904972-6686b180-c14c-11ea-8b33-21d2a34def11.png)


-----문제 유형별 적합한 것-----
1. 모든 정점 방문 : 둘다 가능
2. 경로의 특징 : DFS
3. 최단거리/임의의 경로 : BFS
4. 검색 대상의 규모가 클 때 : DFS
5. 검색 대상의 규모가 작거나, 검색 시작 지점에서 원하는 대상이 별로 멀지 않을 때 : BFS

## 2020. 07. 15(week3)
최단 경로 탐색 중 다익스트라 알고리즘 내용요약

다익스트라(Dijkstra) 알고리즘 
1. 정의

    단일 출발 (single-source shortest path problem) 최단 경로 문제
  
    그래프 내의 특정 노드 u 와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제

2. 알고리즘 (로직)

    첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
  
    너비우선탐색(BFS)와 유사
  
    우선순위 큐를 활용한 다익스트라 알고리즘
 
 ![image](https://user-images.githubusercontent.com/26875426/88520827-14d89500-d02f-11ea-95c5-97aee2afa16b.png)


## 2020.07.27(week4)
그리디 알고리즘 내용요약

그리디 알고리즘(Greedy Algorithm) (a.k.a 탐욕 알고리즘)

1. 정의 : 미리 정한 기준에 따라서 최적의 답을 선택하는 알고리즘

    그리디 알고리즘은 동적계획법(Dynamic Programming)보다 효율적이지만, 반드시 최적의 답을 구하지 못한다.
    주로 근사치 추정을 위해 사용한다. 
    
2. 알고리즘

-1. Selection Procedure : 당시에 가장 최적의 답을 구한 뒤 이를 부분해 집합에 추가한다.

-2. Feasibility Check : 새로운 부분해 집합이 적절한지 검사한다. 

-3. Solution Check : 새로운 부분해 집합이 문제의 답이 맞는지 검사한다. 문제의 답이 완성되지 않았다면 1번부터 다시 시작한다.


3. 활용
  Prim Algorithm, Kruskal Algorithm, Dijkstra Algorithm 등 에서 그리디 알고리즘이 적용 가능하다. 
  
  -1. Prim Algorithm
  
  임의의 정점(vertex)에서 가중치가 가장 작은 간선(edge)을 선택, 
  선택된 정점(vertex)와 연결된 간선(edge)들 중에 가장 가중치가 작은 것들을 선택(단, cycle을 만드는 경우는 제외)
  
  
![image](https://user-images.githubusercontent.com/26875426/88521139-80bafd80-d02f-11ea-945b-11b98b7c5775.png)


  -2.  Kruskal Algorithm
  
  그래프의 모든 간선(edge)중에서 가중치가 가장 작은 것부터 차례대로 선택(단, Cycle을 만드는 경우는 제외)
   
   
![image](https://user-images.githubusercontent.com/26875426/88521158-87497500-d02f-11ea-98b8-12cc38489011.png)

## 2020.07.29(week5)
플로이드 와샬(Floyd Warshall Algorithm) 알고리즘 내용요약

1. 정의 : 모든 정점에서 모든 정점으로의 최단 경로

    음의 가중치를 가진 간선 사용 가능
    
    optimal substructure의 개념을 이용하여 최단 경로를 찾음
    
2. 알고리즘

    -1. 2차원 배열을 만들고 그래프의 간선 정보를 저장(두 정점이 직접적으로 연결되어 있지 않으면 INF(무한대), 자기 자신이면 0)
    
    -2. 경유지 1~V 까지 순회하여 2차원 테이블을 업데이트 
    

![image](https://user-images.githubusercontent.com/26875426/88772528-de7c5080-d1bb-11ea-94b1-30e5b35bd430.png)



