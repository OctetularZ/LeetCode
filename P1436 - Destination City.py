def destCity(self, paths: List[List[str]]) -> str:
    visited = {}
    for path in paths:
        if path[0] in visited:
            pass
        else:
            visited[path[0]] = path[1]
    for value in visited.values():
        if value in visited:
            pass
        else:
            return value