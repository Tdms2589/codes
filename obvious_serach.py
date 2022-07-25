import random

def obvious_search(l,k):
  for i in l:
    if i==k:
      print(i)
      return 1
  return 0
  
randomlist = []
for i in range(0,100):
  n = random.randint(1,30)
  randomlist.append(n)
print(randomlist)
print(obvious_search(randomlist,2))
  
