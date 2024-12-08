def test():
    print("This is test")

test()

def calc(a, b):
    print(a+b)
    print(a-b)
    print(a*b)

calc(3,4)
calc(5,8)
calc(3,4)
calc(4,9)

def pr_calc(a, b=5):
    print(a + b)
    print(a - b)
    print(a * b)

pr_calc(4)
pr_calc(5, 8)