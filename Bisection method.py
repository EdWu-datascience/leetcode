#problem:
#u have product from 1~n, if product i is bad then product i~n are also bad,
#find the first product that's bad 



# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #如果left==True,则right和mid也一定==True
        #possible cases:
        #1 left == F right == T mid == T
        #2 left == F right == T mid == F
        #3 left == T right ==T mid == T
        #in order to decrease time complexity, we use Bisection method
        #为了找出target value,比较 the relationship among left,right and mid
        #then change left == mid or right == mid and recalculate mid
        #time complexity:O(log2n)
        if n == 1:
            return 1 
        flag = 0 
        left = 1
        right = n
        mid = int((left+right)/2)
        while flag == 0:
            if isBadVersion(left) == False and isBadVersion(right) == True and isBadVersion(mid) == False:
                left = mid 
                mid = int((left+right)/2)
                if left + 1 == right:
                    return isBadVersion(left)*left + isBadVersion(right)*right
            elif isBadVersion(left) == False and isBadVersion(right)== True and isBadVersion(mid) == True:
                right = mid
                mid = int((left+right)/2)
                if left + 1 == right:
                    return isBadVersion(left)*left + isBadVersion(right)*right
            elif left == True:
                return left 