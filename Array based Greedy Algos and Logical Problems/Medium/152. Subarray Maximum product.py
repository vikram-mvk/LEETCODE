def maxProduct(self, nums) -> int:
    # positive max stores the largest positive product
    # negative_max stores the largest negative product (when ever a negative number occours it can become the largest positive product)
    ans = negative_max = positive_max = nums[0]  # initially point everything to first element

    for i in range(1, len(nums)):
        temp = positive_max  # since we're overwriting positive max, we will lose it and won't be able to calculate neg_max without temp

        positive_max = max(nums[i], positive_max * nums[i], negative_max * nums[i])
        # it could be the curr num or the product of curr_num and positive max or product of curr_num and negative max (if nums[i] is negative)

        negative_max = min(nums[i], negative_max * nums[i], temp * nums[i])
        # it could be the curr num or the product of curr_num and positive max or product of curr_num and negative max (if nums[i] is positive)

        ans = max(positive_max, ans)

    return ans
