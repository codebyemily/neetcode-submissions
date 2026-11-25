class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        store = Counter(nums)
        # key arg tells max what to compare
        # for current_key in store:
        # comparison_value = store.get(current_key)
        return max(store, key=store.get)