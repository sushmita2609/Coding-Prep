def reversed(str):
  if len(str)==0:
    return str
  else:
    return reverse(s[1:]) + s[0]
str = input()
print(reversed(str))
