def insertion_sort(list):
  for index, value in enumerate(list):
    j = index - 1
    while j >= 0 and value < list[j]:
      list[j+1] = list[j]
      j -= 1
    list[j+1] = value
