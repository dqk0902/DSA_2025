import random

def count_nested(intervals):
    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
    
    stack = []
    nested_count = 0

    for start, end in sorted_intervals:
        while stack and stack[-1][0] >= start:
            nested_count += 1
            stack.pop()
        
        stack.append((start, end))

    return nested_count

if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999