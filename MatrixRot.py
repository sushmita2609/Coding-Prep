# Rotate a matrix by 90'
#  Input:  2 4 5
#          3 4 1
#          3 8 4
# Output: 3 3 2
#         8 4 4
#         4 1 5


def rotate(arr):
    global N
    for j in range(N):
        for i in range(N - 1, -1, -1):
            print(arr[i][j], end = " ")
        print()

N = 3
arr = [[1, 2, 3],
       [5, 6, 7],
       [7, 10, 11]]
rotate(arr)
