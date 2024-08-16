# Reverse Integer - LeetCode
# Define the Solution class with the reverse method
class Solution:
    def reverse(self, x: int) -> int:
        x1 = str(x)
        rev = ""
        for i in range(len(x1) - 1, -1, -1):
            rev += x1[i]
            # Create an instance of the Solution class
        rev_int = int(rev)
        print(rev_int)


solution = Solution()

# Call the reverse method with an integer argument
solution.reverse(123)  # This will print 1, 2, 3, 4
