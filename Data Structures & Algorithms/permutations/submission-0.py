class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(i,n)
                    newPerms.append(pcopy)
            perms = newPerms

        return perms
            

            

            
                