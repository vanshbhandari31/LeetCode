class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        new_string=string[::-1];
        if new_string==string:
            return True
        else:
            return False

