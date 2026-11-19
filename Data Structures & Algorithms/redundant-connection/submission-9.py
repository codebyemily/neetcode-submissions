class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = {i: i for i in range(1, N + 1)} # each node starts off as its own parent 
        rank = {i: 1 for i in range(1, N + 1)} # each node has a rank of 1 (rank = est. height)

        def find(n):
            if n == par[n]:
                return par[n]
            else: 
                return find(par[n])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:  # cycle found 
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True 
        
        for n1, n2 in edges:
            # always gonna be one edge creating a cycle,so no need to check for an else 
            if not union(n1, n2):
                return [n1, n2]

        