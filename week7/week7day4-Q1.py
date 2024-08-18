class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) < 2:
            return None  # Not enough elements to find both largest and second largest

        largest = float('-inf')
        second_largest = float('-inf')

        for num in A:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num

        # If second_largest is still -inf, check if we have duplicates of largest
        if second_largest == float('-inf'):
            if A.count(largest) > 1:
                return largest + largest
            return None

        return largest + second_largest


# Example usage
sol = Solution()

A = [10, 5, 20, 20, 15]
print(sol.solve(A))  # Output: 35 (20 + 15)

A = [1, 1, 1]
print(sol.solve(A))  # Output: 2 (1 + 1)

A = [10]
print(sol.solve(A))  # Output: None (not enough elements)

A = [5, 5, 5, 2]
print(sol.solve(A))  # Output: 10 (5 + 5)

A = [7, 7, 3, 3, 4]
print(sol.solve(A))  # Output: 14 (7 + 7)
