class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = [ele for ele in str(x)]
        return l == l[::-1]