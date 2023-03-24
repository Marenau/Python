from module import GLOBAL_VAR
import module

def f():
    print("Hello 1!")
    print(GLOBAL_VAR)
    print(module.GLOBAL_VAR)

f()