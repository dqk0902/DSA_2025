import time
import random
def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1
        
        if count[x] > count[mode]:
            mode = x
 
    return mode

def find_mode_by_sort(numbers):
    sorted_numbers = sorted(numbers)
    mode = sorted_numbers[0]
    max_count = 1
    current_count = 1

    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] == sorted_numbers[i-1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_count:
            max_count = current_count
            mode = sorted_numbers[i]
    
    return mode

def test_mode_functions(n=10**7, range_start=1, range_end=1000):
    numbers = [random.randint(range_start, range_end) for _ in range(n)]

    start_time = time.time()
    dict_mode = find_mode(numbers)
    dict_time = time.time() - start_time

    start_time = time.time()
    sort_mode = find_mode_by_sort(numbers)
    sort_time = time.time() - start_time

    print(f"  Time: {dict_time:.6f} seconds")
    print(f"  Mode: {dict_mode}")
    print(f"Sorting implementation:")
    print(f"  Time: {sort_time:.6f} seconds")
    print(f"  Mode: {sort_mode}")

    return dict_time, sort_time

if __name__ == "__main__":
    test_mode_functions()