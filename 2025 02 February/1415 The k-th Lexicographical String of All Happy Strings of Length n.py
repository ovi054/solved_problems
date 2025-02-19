class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def followRules(s):
            for i in range(n-1):
                if s[i]==s[i+1]:
                    return False
            return True

        def generate_happy_strings(n):
            happy_strings = []
            for s in product("abc", repeat=n):
                
                if followRules(s):
                    happy_strings.append("".join(s))
            
            return happy_strings
        
        happy_strings = generate_happy_strings(n)

        return happy_strings[k-1] if k<=len(happy_strings) else ""
        