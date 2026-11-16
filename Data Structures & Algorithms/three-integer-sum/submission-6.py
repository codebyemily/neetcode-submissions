class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i + 1 
            k = len(nums) - 1

            # j + k = -i

            # skip duplicate i's
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            

            target = -nums[i] 

            while j < k: 
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1 
                    
                    # skip j and k dups 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1 
                    
                    
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: 
                    j += 1 
        return res
            
        