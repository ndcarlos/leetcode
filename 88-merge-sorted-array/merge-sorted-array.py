class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        stop = n
        for i in range(stop):
            nums1[m+i] = nums2[stop - 1]
            while stop < 0:
                return
            stop -= 1
        nums1.sort()