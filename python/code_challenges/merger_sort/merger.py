def merge_sort(list):
    n = len(list)
    if n <= 1:
        return list

    if n > 1:
        mid = n // 2
        lefty = list[0:mid]
        righty = list[mid:n]
        merge_sort(lefty)
        merge_sort(righty)
        return merge(lefty, righty, list)

def merge(lefty, righty, list):
    i = 0
    j = 0
    k = 0

    while i < len(lefty) and j < len(righty):
        if lefty[i] <= righty[j]:
            list[k] = lefty[i]
            i = i + 1
        else:
            list[k] = righty[j]
            j = j + 1

        k = k + 1

    if i == len(lefty):
        list[k:] = righty[j:] #set remaining entries in arr to remaining values in righty
    else:
        list[k:] = lefty[i:] #set remaining entries in arr to remaining values in lefty
    return list


