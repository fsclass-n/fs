# 표준 출력
'''
    print(값, 값, ..., sep=' ', end='\n')
        sep는 구분자로 기본값은 공백
        end는 끝맞추기 기본값은 \n
'''

print("Life is too short")
print("Life", "is", "too", "short")
# 모두 문자열이면 +는 연결
# 문자열과 숫자의 +는 error
print("Life " + "is " + "too " + "short")
print("2026", "04", "16", sep="-")
'''
Life is too short
Life is too short
Life is too short
2026-04-16
'''

# end의 기본값 \n
print("Life", end="\n")
print("is")
print("too")
print("short")

print("Life", end=" ")
print("is", end=" ")
print("too", end=" ")
print("short")
'''
Life
is
too
short
Life is too short
'''

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=" ")

'''
0
1
2
3
4
0 1 2 3 4
'''