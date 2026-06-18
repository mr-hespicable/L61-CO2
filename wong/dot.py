import math
a = [2, 1]
b = [-3, -1.5]

def dot(u, v):
    s = sum([math.prod(i) for i in zip(u, v)])
    return s

def magnitude(v):
    return math.sqrt(sum(map(lambda x: x**2, v)))

def cos_theta(u, v):
    return (dot(u, v)) / (magnitude(u) * magnitude(v))

def angle_between(u, v):
    return math.acos(cos_theta(u, v))
    
print(dot(a, b))
print(cos_theta(a, b))
print(math.degrees(angle_between(a, b)))
