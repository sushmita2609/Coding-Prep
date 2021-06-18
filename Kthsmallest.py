# Find the Kth smallest element in the given list
# Input: 13 5 7 21 9 4 11
#        4
# Output: 9


def ksmall(arr, k):
    arr.sort()
    res = arr[k - 1]
    return res

def tes():
    t = 0
    ar = []
    print("Value for K:")
    K = int(input())
    print("Size of list:")
    n = int(input())
    print("Enter the numbers:")
    for i in range(n):
        ar.insert(i, int(input()))
    ans = ksmall(ar, K)
    print("The Kth smallest element is:")
    print(ans)
    return t


print("To find the Kth smallest number in the given list, Please enter following values:")
print("Note: The value of K should be less than size of list")
tryAgain = True;
while(tryAgain):
    try:
        tryAgain = tes()
    except ValueError:
        print("Please try with numeric values as input.")
    except IndexError:
        print("The value of K should be smaller than size of list. Try Again!")

