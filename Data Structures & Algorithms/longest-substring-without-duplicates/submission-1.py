class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset=set()
        l=0
        mlen=0

        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l =l + 1
            cset.add(s[r])
            mlen=max(mlen,r-l+1)
        return mlen
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")
        