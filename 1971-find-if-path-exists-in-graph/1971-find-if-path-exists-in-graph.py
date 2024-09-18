from collections import defaultdict

class Solution:
    def check(self, graph: defaultdict, node: int, dest: int, visited: List[bool]) -> bool:
        if node == dest:
            return True
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            if self.check(graph, neighbor, dest, visited):
                return True
        return False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        return self.check(graph, source, destination, visited)

        
