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

        