'''
https://leetcode.com/problems/product-of-array-except-self/

Famous problem, so see multiple approches

Approach 1: Left and right array.
1. Left has the products of array elements to the left of i (fill it from left to right)
2. right has products of array elts to right (fill it from right to left)
3. multiply L and R arrays to get the output array

Approach 2: Same approach with less space
1. Use output array as left array
2. Use a variable to multiply R at each iteration (acts like R array[i] at each i
'''


# Approach 1: Left and Right Array
nums=[1,2,3,4]
N = len(nums)
left = [1] * N
# stores product to the left of i

right = [1] * N
# stores product to the right of i

output = [1] * N

# Fill it from left to right
for i in range(1, N):
    # for every current element, multiply its previous element with num's pre element
    left[i] = left[i - 1] * nums[i - 1]

# Fill it from right to left
for i in range(N - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]

for i in range(0, N):
    output[i] = left[i] * right[i]

print(output)

#Approach 2
N = len(nums)
output = [1] * N

# Fill the output array from left to right to store products of all elts to the left of i
for i in range(1, N):
    # for every current element, multiply left's previous element with num's pre element
    output[i] = output[i - 1] * nums[i - 1]

'''
we need all the right products. We need to start form the last and keep updating the R variable, so that finally at R=0, we have all           the right products
'''
R = nums[N - 1]
# start with the last element as R
# We already have left product in the output array. Just multiply the right with curr element in outout array
for i in range(N - 2, -1, -1):
    output[i] = output[i] * R
    R = R * nums[i]

print(output)

'''

Naturally we tend to use brute force to multiply all products to the left and to the right of current element
for every index which will give TLE
So we need to store the computed value, for ex: [4,3,5,1] for 4 we multiplied other 3 elements and again for 3 we remultiply
the same 2 elements.
One approach is to store the complete product and divide the current element but division is not allowed

'''