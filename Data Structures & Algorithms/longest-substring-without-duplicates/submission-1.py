class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        queue = deque([])
        max_length = 0
        current_length = 0
        seen = set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
               while ch in seen:
                    ele = queue.popleft()
                    seen.remove(ele)
                    current_length -= 1
            queue.append(ch)
            seen.add(ch)
            current_length += 1
            max_length = max(max_length, current_length)
        return max_length
        