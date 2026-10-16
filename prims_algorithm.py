
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 1],
    [6, 8, 1, 0]
]

n = len(graph)
visited = [0] * n
visited[0] = 1
cost = 0

for i in range(n - 1):
    minimum = 999
    x = y = 0

    for j in range(n):
        if visited[j]:
            for k in range(n):
                if not visited[k] and graph[j][k] != 0:
                    if graph[j][k] < minimum:
                        minimum = graph[j][k]
                        x, y = j, k

    print(x, "-", y, ":", minimum)
    cost += minimum
    visited[y] = 1

print("Minimum cost:", cost)

