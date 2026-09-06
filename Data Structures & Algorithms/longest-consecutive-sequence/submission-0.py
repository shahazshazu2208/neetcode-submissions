class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(N) space, removes duplicates
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the START of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Incrementally check for consecutive elements
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

# Example usage:
sol = Solution()
print(sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  # Output: 4 ([2, 3, 4, 5])
print(sol.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))           


            

        