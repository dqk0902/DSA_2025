import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    n = comparer.list_size()
    
    indices = list(range(n))

    sorted_indices = merge_sort(indices, comparer)
    
    result = [0] * n
    for i, idx in enumerate(sorted_indices):
        result[idx] = i + 1
    
    return result

def merge_sort(arr, comparer):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left, comparer)
    right = merge_sort(right, comparer)
    
    return merge(left, right, comparer)

def merge(left, right, comparer):
    result = []
    left_idx = right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if comparer.smaller(left[left_idx], right[right_idx]):
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]