# validate an IP address
# Input: 175.81.35.09
# Output: yes


def valid_add(str):
    flag = 1
    if str.count('.') != 3:
        return 0
    s1 = str.split('.')
    for i in s1:
        if not i.isdigit():
            print("Please enter numeric values")
            flag = 0
            break
        if int(i) < 0 or int(i) > 255 or (i[0] == '0' and len(i) != 1):
            flag = 0
            break
    return flag



print("Validate an IP4 address")
st = input("Enter IPV4 address:")
res = valid_add(st)
if res == 0:
    print("Invalid address")
else:
    print("valid address")


