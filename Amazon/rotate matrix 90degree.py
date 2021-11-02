
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
#DO NOT allocate another 2D matrix and do the rotation.



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        flatten = [i for item in matrix for i in item]
        n = len(matrix)
        #first iteration n=3,-3,-3+(-3), -3+(-3*2)
        #second interation n= ,-3+1,-3+(-3)+1,
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                matrix[i][j] = flatten[-n+(-n)*j+i]
        print(matrix)