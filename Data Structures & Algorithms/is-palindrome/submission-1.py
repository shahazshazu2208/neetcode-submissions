class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=''
        for c in s:
            if c.isalnum():
                ns+=c.lower()
        rs=ns[::-1]
        if rs==ns:
            return True
        else:
            return False

