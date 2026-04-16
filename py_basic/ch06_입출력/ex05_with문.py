target_path = "D:\\wi\git\\fs\\py_basic\\ch06_입출력"

# r(Raw String): 날 머신 문자열
base_path = r"D:\wi\git\fs"

relative_path = "py_basic/ch06_입출력"
full_path = base_path + "/" + relative_path
print(full_path)

f = open(full_path + "/foo1.txt", "w")
f.write("Life is too short, you need python")
f.close()

# with 문
# f를 자동으로 닫는다.
with open(full_path + "/foo2.txt", "w") as f:
    f.write("Life is too short, you need python")


