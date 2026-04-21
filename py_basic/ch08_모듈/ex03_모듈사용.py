# import 파일명1, 파일명2, ...
import mod2, mod1
from other import mod3
# import mod1

print(mod2.PI) # 3.141592
a = mod2.Math() 
print(a.solv(2)) # 12.566368
print(mod2.add(mod2.PI, 4.4)) # 7.5415920000000005


print(mod1.add(3, 4)) # 7
print(mod1.sub(3, 4)) # -1
print(mod3.mul(3, 4)) # 12
