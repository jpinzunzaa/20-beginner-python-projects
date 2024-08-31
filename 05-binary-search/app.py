def binary_search(list, element):
  middle = 0
  start = 0
  end = len(list)
  steps = 0

  while (start <= end):
    steps = steps + 1
    middle = (start + end) // 2
    if element == list[middle]:
      return middle
    if element < list[middle]:
      end = middle - 1
    else:
      start = middle + 1
  
  return -1