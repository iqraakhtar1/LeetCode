class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        
        # Create a 2D array to store the length of the longest common subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp array using bottom-up dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The result is stored in the bottom-right cell of the dp array
        return dp[m][n]
#         count = 0
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i] == text2[j]:
#                     count+=1
               
#         return count
        
#         dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

#         for i in range(len(text1)-1, -1, -1):
#             for j in range(len(text2)-1,-1,-1):
#                 if text1[i]==text2[j]:
#                     dp[i][j]= 1+dp[i+1][j+1]
#                 else:
#                     dp[i][j] =max(dp[i][j+1], dp [i+1][j])
#         return dp[0][0]

