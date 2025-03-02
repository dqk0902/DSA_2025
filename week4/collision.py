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
    A = 23
    M = 2**32
    target_hash = hash_value(string)

    def backtrack(current_string, current_hash):
        if current_hash == target_hash and current_string != string:
            return current_string
        
        if len(current_string) >= 10:
            return None

        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_string = current_string + char
            char_value = ord(char) - ord('a')
            new_hash = (current_hash * A + char_value) % M
            
            result = backtrack(new_string, new_hash)
            if result:
                return result

        return None

    result = backtrack('', 0)
    return result if result else 'notfound'

if __name__ == "__main__":
    string1 = "vutiwg"
    string2 = find_other("vutiwg")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682