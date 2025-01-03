class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        preMap = set()
        for i in nums:
            if i in preMap:
                return True
            else:
                preMap.add(i)
        return False
