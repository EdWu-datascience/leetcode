#方法原理
#https://leetcode-cn.com/problems/product-of-array-except-self/solution/product-of-array-except-self-shang-san-jiao-xia-sa/998479
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        right_product = [1]
        for i in nums[0:len(nums)-1]:
            left_product.append(left_product[-1]*i)
        for j in nums[::-1][0:len(nums)-1]:
            right_product.append(right_product[-1]*j)
        right_product = right_product[::-1]
        re = []
        for index,value in enumerate(left_product):
            re.append(value*right_product[index])
        print(re)
        return re 