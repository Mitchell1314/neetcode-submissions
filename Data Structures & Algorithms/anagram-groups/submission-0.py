class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = dict()
        for word in strs:
            pattern = self.anagram_pattern(word)
            if pattern in result:
                result[pattern].append(word)
            else:
                result[pattern] = [word]
        return list(result.values())

    def anagram_pattern(self, word):
        pattern = dict()
        for ch in word:
            if ch not in pattern:
                pattern[ch] = 1
            else:
                pattern[ch] += 1
        pattern = tuple(sorted(pattern.items()))
        return pattern




  


        