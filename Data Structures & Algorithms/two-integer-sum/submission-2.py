class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """output=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
                    return output"""
        hashmap={}
        output=[]
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            complement= target- nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                output.append(hashmap[complement])
                output.append(i)
                output.sort()
                return output