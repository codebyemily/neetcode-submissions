from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        best_length = float('inf')
        best_start = 0
        freq = Counter(t) 
        window = Counter()
        need = len(freq)
        formed = 0

        while r < len(s):
            if s[r] in freq: 
                window[s[r]] += 1
                if window[s[r]] == freq[s[r]]:
                    formed += 1

            # remove l until invalid 
            while formed == need: 
                if s[l] in freq: 
                    window[s[l]] -= 1 

                    # update the best_start 
                    
                    if r - l + 1 < best_length:
                        best_length = r - l + 1
                        best_start = l
                    
                    if window[s[l]] < freq[s[l]]:
                        formed -= 1
                    
                l += 1
                        
            
            r += 1
        return "" if best_length == float('inf') else s[best_start: best_start + best_length] 