class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        sorted_s=sorted(s)
        sorted_t=sorted(t)
        if sorted_s==sorted_t:
            return True
        else:
            return False
        """
        count=defaultdict(int)
        for x in s:
            count[x]+=1
        for x in t:
            count[x]-=1
        for val in count.values():
            if val !=0:
                return False
        return True
