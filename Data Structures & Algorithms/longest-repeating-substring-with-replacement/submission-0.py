class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        mc = 0
        ml = 0
        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c,0)+1
            mc = max(mc,count[c])

            while (right - left + 1) - mc > k:
                lc = s[left]
                count[lc] -= 1
                left += 1
            ml = max(ml,right-left+1)
        return ml
sol = Solution()
print(sol.characterReplacement("XYYX", 2))     # Output: 4
print(sol.characterReplacement("AAABABB", 1))  # Output: 5
        