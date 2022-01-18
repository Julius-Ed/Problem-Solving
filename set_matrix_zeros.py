"""
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in range(len(matrix)):
            row_trailer = False
            for column in range(len(matrix[row])):

                if matrix[row][column] == 0:
                    row_trailer = "True"

                if row_trailer and matrix[row][column] != 0:
                    matrix[row][column] = "True"

        for column in range(len(matrix[0])):
            column_trailer = False

            for row in range(len(matrix)):

                if matrix[row][column] == 0:
                    column_trailer = "True"

                if column_trailer and matrix[row][column] != 0:
                    matrix[row][column] = "True"

        # reverse row looping
        for row in range(len(matrix) - 1, -1, -1):
            row_trailer = False
            for column in range(len(matrix[row]) - 1, -1, -1):

                if matrix[row][column] == 0:
                    row_trailer = "True"

                if row_trailer and matrix[row][column] != 0:
                    matrix[row][column] = "True"

        # reverse columns looping
        for column in range(len(matrix[0]) - 1, -1, -1):
            column_trailer = False

            for row in range(len(matrix)-1, -1, -1):

                if matrix[row][column] == 0:
                    column_trailer = "True"

                if column_trailer and matrix[row][column] != 0:
                    matrix[row][column] = "True"

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == "True":
                    matrix[row][column] = 0    



Sol = Solution()

matrix = [
    [1, 0, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]


# Sol.setZeroes(matrix)
# print(matrix)


Sol2.setZeroes(matrix)
print(matrix)
