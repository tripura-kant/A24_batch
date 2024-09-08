class Solution:
    def sumOfDivisors(self, N):
        # Helper function to calculate the sum of divisors of a single number
        def sum_of_divisors(x):
            total = 0
            for i in range(1, x + 1):
                if x % i == 0:
                    total += i
            return total

        # Initialize the total sum for all numbers from 1 to N
        total_sum = 0

        # Compute the sum of divisors for each number from 1 to N
        for i in range(1, N + 1):
            total_sum += sum_of_divisors(i)

        return total_sum


# Example usage
sol = Solution()
print(sol.sumOfDivisors(4))  # Output: 28 (1 + (1+2) + (1+2+4) + (1+2+4))
