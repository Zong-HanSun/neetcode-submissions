class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        num_iteration_needed = len(s) / 2
        i = 0
        while i < num_iteration_needed:
            s = s.replace("()" , "")
            s = s.replace("[]" , "")
            s = s.replace("{}" , "")
            i +=1
        
        return not s

        