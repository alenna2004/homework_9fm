def find_value(nums,value):
    if not nums or value > nums[-1] or value < nums[0]:
        return False
    if value == nums[0] or value == nums[-1]:
        return True
    left = 0
    right = len(nums)
    while right - left > 3:
        mid = len(nums[left: right])//2
        if value < nums[mid]:
            right = mid
        else:
            left = mid
    return value in nums[left:right]
