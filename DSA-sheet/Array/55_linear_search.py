class Solution:
    def searchInSorted(self, arr, k):
        for i in range(0, len(arr)):
            if arr[i] == k:
                return True
        return False


arr = [1, 2, 3, 4, 6]
k = 5

result = Solution()

print(result.searchInSorted(arr, k))
