def mergeTwoArray(nums1, nums2):
    for x in range(0, len(nums2)):
        i = x + len(nums1)
        nums1[i] = nums2[x]
    nums1.sort()
    return nums1


print(mergeTwoArray([1, 2, 3, 0, 0, 0], [2, 5, 6]))
