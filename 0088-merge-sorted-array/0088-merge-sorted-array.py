class Solution:
    def merge(self, nums1, m, nums2, n):
        # Start from the end of both arrays
        i = m - 1  # last element in nums1's actual values
        j = n - 1  # last element in nums2
        k = m + n - 1  # last position in nums1 (total size)

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
