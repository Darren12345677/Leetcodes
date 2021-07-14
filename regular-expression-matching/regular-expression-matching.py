class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            if not s and not p:
                return True
            elif p and "*" == p[-1]:
                return self.isMatch(s, p[:-2])
            else:
                return False
        elif p[-1] == "*":
            if p[-2] == s[-1] or p[-2] == ".":
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p) or self.isMatch(s[:-1], p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        elif p[-1] == s[-1] or p[-1] == ".":
            return self.isMatch(s[:-1], p[:-1])
        else:
            return False