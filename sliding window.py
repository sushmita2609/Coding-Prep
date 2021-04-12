def sliding(win, k):
  t=0
  for i in range(len(win) -k +1):
    temp = 0
    for i in range(k):
      temp=temp+win[i+k]
    if(temp>t):
      t = temp
  return t
win = [4,6,2,8,1,2,9,6]
k=4
print(sliding(win,k))
