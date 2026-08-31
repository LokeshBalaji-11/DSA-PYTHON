class Solution():

    def largest_prefix(self, arr):

        result = ""
        a = 0

        for i in range(len(arr[a])):

            for j in range(1, len(arr)):

                if arr[a][i] == arr[j][i]:

                    if j == len(arr) - 1:
                        result += arr[a][i]

                else:
                    return result

        return result


a = Solution()
x=Solution()
b = ["geeksforgeeks", "geeks", "geek", "geezer"]
c = ["hello", "world"]

print(a.largest_prefix(b))
print(x.largest_prefix(c))