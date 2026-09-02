import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for chars in s:
            if chars not in string.ascii_letters and chars not in string.digits:
                s = s.replace(chars, "")
        
        return s.lower() == s[::-1].lower()

       