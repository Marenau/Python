from one import f
from module import GLOBAL_VAR
import module

def g():
    print("Hello 2!")
    print(GLOBAL_VAR)
    print(module.GLOBAL_VAR)

f()
print()
g()
print()
GLOBAL_VAR = 10
module.GLOBAL_VAR = 17
g()
print()
f()