# sorted
# sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 새로운 리스트로 반환
lst = [3,1,2]

print(lst) # [3, 1, 2]
print(sorted(lst)) # [1, 2, 3]
print(lst) # [3, 1, 2]

print(lst.sort()) # None
print(lst) # [1, 2, 3]


print('-'*30)
print(sorted(['a','c','b'])) # ['a','b','c']
print(sorted("zero")) # ['e','o','r','z']
print(sorted((3, 2, 1))) # [1, 2, 3]