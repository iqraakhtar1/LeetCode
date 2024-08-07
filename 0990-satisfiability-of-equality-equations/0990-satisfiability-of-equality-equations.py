class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [0] * 26
        rank = [0] * 26

        def make_set(n):
            for i in range(n):
                parent[i] = i
                rank[i] = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
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

        # Initialize parent and rank arrays
        make_set(26)

        # Process all equations of the type "a==b"
        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

        # Process all equations of the type "a!=b"
        for eq in equations:
            if eq[1] == '!':
                if find(ord(eq[0]) - ord('a')) == find(ord(eq[3]) - ord('a')):
                    return False

        return True
