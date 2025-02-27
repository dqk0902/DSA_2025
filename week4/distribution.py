def create_distribution(string):
    substrings = set()
    
    n = len(string)
    
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = string[start:end]
            substrings.add(substring)
    
    distribution = {}
    
    for substring in substrings:
        length = len(substring)
        if length in distribution:
            distribution[length] += 1
        else:
            distribution[length] = 1
    
    return distribution

if __name__ == "__main__":
    print(create_distribution("aaaa"))  # {1: 1, 2: 1, 3: 1, 4: 1}
    print(create_distribution("abab"))  # {1: 2, 2: 2, 3: 2, 4: 1}
    print(create_distribution("abcd"))  # {1: 4, 2: 3, 3: 2, 4: 1}
    print(create_distribution("abbbbbb"))  # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}
    print(create_distribution("aybabtu"))  # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}