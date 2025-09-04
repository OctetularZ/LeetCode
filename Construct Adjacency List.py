def construct(edges, nodes):
  adj = {}
  for i in edges:
    neighbours = adj.get(i[0], [])
    neighbours.append(i[1])
    adj[i[0]] = neighbours

    neighbours = adj.get(i[1], [])
    neighbours.append(i[0])
    adj[i[1]] = neighbours
  
  return adj
    


n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]

print(construct(edges, n))


# Alternate method
def build_adj_list(n, edges):
    adj_list = {i: [] for i in range(n)}

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    return adj_list
