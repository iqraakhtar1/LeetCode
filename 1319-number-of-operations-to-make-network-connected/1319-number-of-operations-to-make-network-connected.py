class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = []
        rank = []
        
        def make_set(k):
            nonlocal parent, rank
            parent = [i for i in range(k)]
            rank = [0] * k
            
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                return
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
        
        if len(connections) < n - 1:
            return -1
        
        make_set(n)
        component = n
        for v in connections:
            if find(v[0]) != find(v[1]):
                union(v[0], v[1])
                component -= 1
        
        return component - 1
