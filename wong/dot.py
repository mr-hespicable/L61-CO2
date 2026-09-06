import math
a = [-1, 2, 4]
b = [3, 5, 5]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def dot(u, v):
    s = sum([math.prod(i) for i in zip(u, v)])
    return s

def magnitude(v):
    return math.sqrt(sum(map(lambda x: x**2, v)))

def cos_theta(u, v):
    return (dot(u, v)) / (magnitude(u) * magnitude(v))

def angle_between(u, v):
    return math.acos(cos_theta(u, v))
    
#print(dot(a, b))
print(math.degrees(angle_between(a, b)))
#print(angle_between(a, b))
