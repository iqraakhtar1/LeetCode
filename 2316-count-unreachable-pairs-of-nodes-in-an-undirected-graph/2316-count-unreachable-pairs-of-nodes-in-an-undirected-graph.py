class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        # Union all nodes connected by edges
        for u, v in edges:
            union(u, v)

        # Count the size of each connected component
        component_size = {}
        for i in range(n):
            root = find(i)
            if root in component_size:
                component_size[root] += 1
            else:
                component_size[root] = 1

        # Calculate the number of unreachable pairs
        result = 0
        remainder = n
        for size in component_size.values():
            result += size * (remainder - size)
            remainder -= size

        return result
