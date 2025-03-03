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
    
    def generate_string(prefix, remaining_length, current_hash):
        if remaining_length == 0:
            if current_hash == target_hash and prefix != string:
                return prefix
            return None
        
        start_char = ord('a') if len(prefix) > 0 else ord(string[0])
        for char_code in range(start_char, ord('z') + 1):
            char = chr(char_code)
            new_hash = (current_hash * 23 + (char_code - ord('a'))) % (2**32)
            result = generate_string(prefix + char, remaining_length - 1, new_hash)
            if result:
                return result
        return None

    # Try strings of the same length as the input
    return generate_string('', len(string), 0) or 'notfound'

if __name__ == "__main__":
    string1 = "vutiwg"
    string2 = find_other("vutiwg")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682