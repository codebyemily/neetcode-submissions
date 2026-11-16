class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {} # key (sorted) --> string 

        for s in strs: 
            sort = sorted(s)
            sort = "".join(sort)
            if sort not in hmap: 
                hmap[sort] = []
            hmap[sort].append(s)
        return list(hmap.values())
