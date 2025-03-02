def hash_value(string):
    A = 23
    M = 2**32
    
    result = 0
    n = len(string)
    
    for i, char in enumerate(string):
        char_value = ord(char) - ord('a')
        
        power = n - 1 - i
        
        result += char_value * (A ** power) # char_value * A^power
    
    return result

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("zfgjynuk")) # 85902251602
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440