class Solution:
    def Distance(self, arr, x, y):
        xd = -1
        yd = -1
        min_distance = float('inf')

        for i in range(len(arr)):
            if arr[i] == x:
                xd = i

            elif arr[i] == y:
                yd = i

            if xd != -1 and yd != -1:
                min_distance = min(min_distance, abs(yd - xd))

        if min_distance != float('inf'):
            return min_distance
        else:
            return -1


arr1 = [1, 2, 3, 2]
arr2 = [86, 39, 90, 67, 84, 66, 62]

s = Solution()

print(s.Distance(arr1, 1, 2))
print(s.Distance(arr2, 42, 12))