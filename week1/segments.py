def find_segments(data):
    result = []
    count = 0

    for i in range(len(data) - 1):
        count += 1
        if data[i] != data[i+1]:
            result.append((count, data[i]))
            count = 0
    
    return result + [(count + 1, data[-1])]
    
if __name__ == "__main__":
    # Test cases
    print(find_segments("aaabbccdddd"))
    # Expected: [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # Expected: [(20, 'a')]

    print(find_segments("abcabc"))
    # Expected: [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("cat"))
    # Expected: [(1, 'c'), (1, 'a'), (1, 't')]

    print(find_segments("mmzxzj"))