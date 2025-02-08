def find_kth_largest(nums: list, k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]

# Example
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
