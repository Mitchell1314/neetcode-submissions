class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack =[]
        stack_1= []
        for ch in s:
            if ch.isalnum():
                stack.append(ch.lower())
        reverse_s = s[::-1]
        for ch in reverse_s:
            if ch.isalnum():
                stack_1.append(ch.lower())
        return stack==stack_1

        