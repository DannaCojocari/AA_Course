def dfs(adj_matrix):
    visited = [False] * len(adj_matrix)
    result = []

    def dfs_recursive(node):
        visited[node] = True
        result.append(node)
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs_recursive(neighbor)

    dfs_recursive(0)
    return result
