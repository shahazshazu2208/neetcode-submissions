from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2= len(s1),len(s2)

        if l1>l2:
            return False

        count = Counter(s1)
        k = Counter(s2[:l1])

        if k == count:
            return True
        
        for right in range(l1,l2):
            k[s2[right]] += 1
            k[s2[right-l1]] -= 1

            if k[s2[right-l1]] == 0:
                del k[s2[right-l1]]
            
            if k == count:
                return True
        return False



        