class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        
        if len(t) > n:
            return ""
        
        # Store the character counts for t
        char_count = Counter(t)
        
        required_count = len(t)
        i, j = 0, 0
        min_window_size = float('inf')
        start_i = 0
        
        # Start sliding the window
        while j < n:
            ch = s[j]
            
            # If character is in the count dictionary and it contributes to required characters
            if ch in char_count and char_count[ch] > 0:
                required_count -= 1
            
            # Decrement the character count in dictionary
            char_count[ch] = char_count.get(ch, 0) - 1
            
            # Shrink the window when required count is zero
            while required_count == 0:
                curr_window_size = j - i + 1
                
                if min_window_size > curr_window_size:
                    min_window_size = curr_window_size
                    start_i = i
                
                start_char = s[i]
                char_count[start_char] = char_count.get(start_char, 0) + 1
                
                if start_char in char_count and char_count[start_char] > 0:
                    required_count += 1
                
                i += 1
            
            j += 1
        
        return "" if min_window_size == float('inf') else s[start_i:start_i + min_window_size]
#         if t == "":
#             return ""

#         countT, window = {}, {}
#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have, need = 0, len(countT)
#         res, resLen = [-1, -1], float("infinity")
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 # update our result
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1
#                 # pop from the left of our window
#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("infinity") else ""