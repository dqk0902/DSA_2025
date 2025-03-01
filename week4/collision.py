def hash_value(string):
    A = 23
    M = 2**32
    
    result = 0
    n = len(string)
    
    for i, char in enumerate(string):
        char_value = ord(char) - ord('a')
        
        power = n - 1 - i
        
        result += char_value * (A ** power)
    
    return result % M

def find_other(string):
    target_hash = hash_value(string)
    
    n = len(string)
    
    for i in range(n):
        original_char = string[i]
        for new_char in 'abcdefghijklmnopqrstuvwxyz':
            if new_char != original_char:
                new_string = string[:i] + new_char + string[i+1:]
                if hash_value(new_string) == target_hash:
                    return new_string
    
    return string 

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682