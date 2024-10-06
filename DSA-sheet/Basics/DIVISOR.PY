# User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
        Sum = 0
        for i in range(1, N + 1):
            Sum += i * (N // i)
        return Sum
