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
