from collections import deque

def bfs(adj_list):
    visited = [False] * len(adj_list)
    result = []
    queue = deque([0])
    visited[0] = True

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result
