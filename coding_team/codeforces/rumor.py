from collections import defaultdict

n, m = map(int, input().split())
c = list(map(int, input().split()))

# building graph
graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

min_cost = float('inf')
print(min_cost)
seen = set()

def dfs(i):
    global min_cost
    min_cost = min(min_cost, c[i - 1])
    seen.add(i)
    for j in graph[i]:
        if j not in seen:
            dfs(j)

res = 0

for i in range(1, n+1):
    if i not in seen:
        dfs(i)

        res += min_cost
        min_cost = float('inf')

print(res)
