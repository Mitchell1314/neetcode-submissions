class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = dict()
        for ch in s:
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
        for ch in t:
            if ch not in result:
                return False
            else:
                result[ch] -= 1
        for re in result:
            if result[re] != 0:
                return False
        return True

