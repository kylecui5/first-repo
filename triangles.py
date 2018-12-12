import math

def hypotenuse(s1, s2):
    return math.sqrt((s1*s1)+(s2*s2))

for i in range(1, 10):
    for j in range(1, 10):
        print(i)
        print(j)
        print(hypotenuse(i, j))