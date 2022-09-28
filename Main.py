from typing import List

def insertionSort(array) -> List[int]:
  for i in range(1,n):
    j = i-1
    t = A[j]
  while A[j]>=0 && A[j]>t
    j = j-1
    A[j+1] = A[j]
    A[j+1] = t

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
