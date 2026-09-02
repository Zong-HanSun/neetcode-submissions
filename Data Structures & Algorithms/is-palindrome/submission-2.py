class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left +=1
                    right -=1
                else:
                    return False

            if s[left].isalnum() and not s[right].isalnum():
                right -=1

            if not s[left].isalnum() and s[right].isalnum():
                left +=1

            if not s[left].isalnum() and not s[right].isalnum():
                left +=1
                right -=1
        
        return True




        