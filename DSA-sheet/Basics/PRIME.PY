# User function Template for python3
from math import sqrt


class Solution:
    def isPrime(self, N):
        # code here
        num = N
        if num == 1:
            return 0
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 1
   