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
    original_hash = hash_value(string)
    target = original_hash + (1 << 32)
    
    powers = []
    current_power = 1 
    while current_power <= target:
        powers.append(current_power)
        next_power = current_power * 23
        if next_power > target:
            break
        current_power = next_power
    
    powers = list(reversed(powers))
    
    coefficients = []
    remaining = target
    for power in powers:
        coeff = remaining // power
        if coeff > 25:
            coeff = 25
        coefficients.append(coeff)
        remaining -= coeff * power
    
    collision_chars = [chr(coeff + ord('a')) for coeff in coefficients]
    collision_str = ''.join(collision_chars)
    
    if collision_str != string:
        return collision_str
    else:
        return collision_str + 'a'

if __name__ == "__main__":
    string1 = "vuitjm"
    string2 = find_other(string1)
    print(string1, hash_value('vuitjm')) # kissa 2905682
    print(string2, hash_value('avuitjm')) # zfgjynuk 2905682