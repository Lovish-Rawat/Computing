import math
print("sin values")
for i in range (0, 346, 15):
    a = math.sin(math.radians(i))
    c = round(a, 4)
    print(c)
print("cosine values")
for i in range(0, 346, 15):
        b = math.cos(math.radians(i))
        t = round(b, 4)
        print(t)

