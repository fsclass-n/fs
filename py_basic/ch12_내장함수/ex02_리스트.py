# 내장 함수
# append(): 리스트의 끝에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]

a.append([5,6])
print(a) # [1, 2, 3, 4, [5, 6]]

# insert(인덱스, 아이템): 요소 삽입
a = [1, 2, 3]
a.insert(0, 4) # 0번 인덱스에 4를 삽입
print(a) # [4, 1, 2, 3]
a.insert(3, 5)
print(a) # [4, 1, 2, 5, 3]
a.insert(5, 6)
# a.append(6)
print(a) # [4, 1, 2, 5, 3, 6]

# remove(값): 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a) # [1, 2, 1, 2, 3]
a.remove(3)
print(a) # [1, 2, 1, 2]

# pop(): 마지막 요소 꺼내기
a = [1, 2, 3]
print(a.pop()) # 3
print(a) # [1, 2]
# pop(인덱스): 인덱스에 해당하는 요소 꺼내기
a = [10, 20, 30]
print(a.pop(1)) # 20
print(a) # [10, 30]

# count(값): 값에 해당하는 항목 개수
a = [1, 20, 31, 1, 20, 1, 1]
print(a.count(20)) # 2

# extend(): 리스트 확장
a = [1, 2, 3]

# a.extend([4, 5])
a += [4, 5]

print(a) # [1, 2, 3, 4, 5]
b = [6, 7]
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7]




print("-----------------------")

# sort(): 정렬 - 오름차순
a = [1, 4, 3, 2]
a.sort()
print(a) # [1, 2, 3, 4]

a = ['b', 'c', 'a']
a.sort()
print(a) # ['a', 'b', 'c']

# reverse(): 역순
a = [1, 4, 3, 2]
a.reverse()
print(a) # [2, 3, 4, 1]

# 내림차순
a.sort()
print(a) # [1, 2, 3, 4]
a.reverse()
print(a) # [4, 3, 2, 1]

# a = [1, 4, 3, 2]
# a.sort().reverse() # error
# print(a)

# index(항목): 인덱스 반환
a = [10, 5, 31]
print(a.index(31)) # 2
print(a.index(5)) # 1
# print(a.index(1)) # error