class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            left = mergeSort(left)
            right = mergeSort(right)

            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                elif left[i] > right[j]:
                    arr[k] = right[j]
                    j += 1
                k += 1
            for g in range(i, len(left)):
                arr[k] = left[g]
                k += 1
            for h in range(j, len(right)):
                arr[k] = right[h]
                k += 1

            return arr

        return mergeSort(nums)
        