# 1. 파일 생성
# 생성 위치: 작업 영역 폴더
'''
    파일 열기 모드
        r : read(읽기)
        w : write(쓰기)
        a : append(추가)
'''
'''
    \n
    \t
    \'
    \"
    \\
'''
# 절대 경로
'''
    http://~
    https://~
    C:~
    D:~
'''
# f = open("D:\\wi\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "w")
# f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "w")
# f.close()


# 2. 파일 쓰기
f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "w", encoding="utf-8")
f.write("Life is too short\n")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# 3. 파일 읽기
'''
    read(): 파일의 전체 내용을 문자열로 읽기
    readline(): 파일의 한(첫) 줄을 문자열로 읽기
    readlines(): 파일의 전체 내용을 리스트로 읽기
'''
f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()


f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
line = f.readline()
print(line)
f.close()


f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


# strip(): 공백 제거
f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
lines = f.readlines()
print(lines)
for line in lines:
    line = line.strip()
    print(line)
f.close()

print("-" * 30)
f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
for line in f:
    line = line.strip()
    print(line)
f.close()


# 4. 파일에 내용 추가 
f = open("D:/wi/git/fs/py_basic/ch06_입출력/newfile.txt", "a", encoding="utf-8")
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()






