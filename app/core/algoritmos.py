def merge_sort(arr, key="score"):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    while left and right:
        if left[0][key] <= right[0][key]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def busqueda_binaria(arr, valor, key="dni"):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == valor: return arr[mid]
        elif arr[mid][key] < valor: low = mid + 1
        else: high = mid - 1
    return None