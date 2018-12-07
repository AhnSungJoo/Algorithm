#BOJ 14754 Pizza Boxes 

x,y = map(int,input().split()) #map은 함수와 반복가능한 자료형을 함께 쓸 수 있다. 공백을 둔 여러 입력을 받기 위해 사용
arr = []
arr2 = set() #각 row에 최대값을 저장한다. 최대값은 중복될 수 있기때문에 set자료형을 사용한다. 
#중복제거를 위해 set을 사용
for i in range(x):
    row = list(map(int,input().split())) #각 row를 한번에 받고 리스트 형으로 저장
    arr2.add(max(row)) #set 자료형에 각 row 최대값을 추가한다.
    arr.append(row) 
for j in range(y):
    arr2.add(max(arr[i][j] for i in range(x))) #각 column에 최대값을 추가한다.
print(sum(map(sum,arr)) - sum(arr2)) #최대값 - 나머지값 
