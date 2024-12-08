import time
import random

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

numbers = [random.randint(1, 1000) for _ in range(10**7)]


start_time = time.time()
count_even_1(numbers)
end_time = time.time()
time_1 = end_time - start_time
print(f"Implementation 1 time: {time_1:.4f} seconds")

start_time = time.time()
count_even_2(numbers)
end_time = time.time()
time_2 = end_time - start_time
print(f"Implementation 2 time: {time_2:.4f} seconds")