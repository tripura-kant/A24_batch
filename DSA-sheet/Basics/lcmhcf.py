import math


class Solution:
    def lcmAndGcd(self, A, B):
        # Compute the GCD using Python's built-in function
        gcd = math.gcd(A, B)

        # Compute the LCM using the formula
        lcm = abs(A * B) // gcd

        # Return the results as a list
        return [lcm, gcd]


A = 14
B = 8

sol = Solution()
print(sol.lcmAndGcd(A, B))
