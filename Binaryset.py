# To validate if string is binary or not
# Input:  1010100         1562544       ss8980
# Output: valid           Invalid       Invalid


def check():
    string = input()
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("valid")
    else:
        print("Invalid")
    return 0


print("To validate if string is binary or not")
print("enter string to check")
tryAgain = True;
while(tryAgain):
    try:
        tryAgain = check()
    except ValueError:
        print("Please try with numeric values as input.")
