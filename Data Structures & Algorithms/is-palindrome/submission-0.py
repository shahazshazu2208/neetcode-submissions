class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=''
        for c in s:
            if c.isalnum():
                ns = ns+c.lower()
        rs=ns[::-1]
        if rs==ns:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw"))