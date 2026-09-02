class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_substring = ""
        t_hashtable = {}

        for c in t:
            if c in t_hashtable:
                t_hashtable[c]+= 1
            else:
                t_hashtable[c] = 1
        
        for i in range(len(s)):
            s_hashtable = {}
            current_substring = ""
            for j in range(i, len(s)):
                current_substring+= s[j]

                if s[j] in s_hashtable:
                    s_hashtable[s[j]]+= 1
                else:
                    s_hashtable[s[j]] = 1

                for key, value in t_hashtable.items():
                    if key not in s_hashtable or t_hashtable[key] > s_hashtable[key]:
                        break
                else:
                    # only reaches here if no breaks happen
                    # thus allowing us to know if substring is valid
                    if len(current_substring) < len(shortest_substring) or not shortest_substring:
                        shortest_substring = current_substring
                    
        return shortest_substring   
        
        