import time
import random

def count_rounds_list(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

def count_rounds_dict(numbers):
    n = len(numbers)
    pos = {}

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

def test_performance(n):
    numbers = list(range(1, n+1))
    random.shuffle(numbers)
    
    start_time = time.time()
    result_list = count_rounds_list(numbers)
    list_time = time.time() - start_time
    
    start_time = time.time()
    result_dict = count_rounds_dict(numbers)
    dict_time = time.time() - start_time
    
    assert result_list == result_dict, "Different results!"
    
    return {
        "n": n,
        "list_time": list_time,
        "dict_time": dict_time,
        "result": result_list
    }
    


if __name__ == "__main__":
    print(test_performance(10**7))