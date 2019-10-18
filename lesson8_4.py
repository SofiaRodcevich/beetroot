#Написать функцию пересечения и функцию объединения неограниченного количества последовательностей

#intersection
aa = [1, 2, 3, 4, 5]
bb = [3, 4, 5, 6, 7]
cc = []
dd = []

def combine(aa, bb, cc):
  for i in bb:
    for j in aa:
      if i == j:
        cc.append(i)
  print(cc)

combine(aa, bb, cc)

def remove(aa, bb, dd):
  for i in aa:
    if i not in bb:
      dd.append(i)

  for j in bb:
    if j not in aa:
      dd.append(j)
  print(dd)

remove(aa, bb, dd)
