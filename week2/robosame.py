def calculate(input, rules):
    symbols = ["L"] + list(input) + ["R"]

    pos = 0
    state = 1
    counter = 0

    while True:
        found = False

        for old_symbol, old_state, new_symbol, new_state, action in rules:
            if symbols[pos] == old_symbol and state == old_state:
                found = True
                counter += 1

                symbols[pos] = new_symbol
                state = new_state

                if action == "RIGHT": pos += 1
                if action == "LEFT": pos -= 1
                if action == "ACCEPT": return True
                if action == "REJECT": return False

                if pos < 0 or pos >= len(symbols):
                    return False

                break

        if not found or counter == 1000:
            return False

def create_rules():
    rules = []
    rules.append(("L", 1, "L", 2, "RIGHT"))
    
    rules.append(("0", 2, "A", 3, "RIGHT"))
    rules.append(("1", 2, "B", 4, "RIGHT"))
    
    rules.append(("0", 3, "0", 3, "RIGHT"))
    rules.append(("1", 3, "1", 3, "RIGHT"))
    rules.append(("A", 3, "A", 3, "RIGHT"))
    rules.append(("B", 3, "B", 3, "RIGHT"))
    rules.append(("C", 3, "C", 3, "RIGHT"))
    rules.append(("D", 3, "D", 3, "RIGHT"))
    rules.append(("R", 3, "R", 5, "LEFT"))
    
    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("1", 4, "1", 4, "RIGHT"))
    rules.append(("A", 4, "A", 4, "RIGHT"))
    rules.append(("B", 4, "B", 4, "RIGHT"))
    rules.append(("C", 4, "C", 4, "RIGHT"))
    rules.append(("D", 4, "D", 4, "RIGHT"))
    rules.append(("R", 4, "R", 6, "LEFT"))
    
    rules.append(("0", 5, "C", 7, "LEFT"))
    rules.append(("1", 5, "1", 5, "LEFT"))
    rules.append(("A", 5, "A", 5, "LEFT"))
    rules.append(("B", 5, "B", 5, "LEFT"))
    rules.append(("C", 5, "C", 5, "LEFT"))
    rules.append(("D", 5, "D", 5, "LEFT"))
    
    rules.append(("1", 6, "D", 7, "LEFT"))
    rules.append(("0", 6, "0", 6, "LEFT"))
    rules.append(("A", 6, "A", 6, "LEFT"))
    rules.append(("B", 6, "B", 6, "LEFT"))
    rules.append(("C", 6, "C", 6, "LEFT"))
    rules.append(("D", 6, "D", 6, "LEFT"))
    
    rules.append(("0", 7, "0", 7, "LEFT"))
    rules.append(("1", 7, "1", 7, "LEFT"))
    rules.append(("A", 7, "A", 7, "LEFT"))
    rules.append(("B", 7, "B", 7, "LEFT"))
    rules.append(("C", 7, "C", 7, "LEFT"))
    rules.append(("D", 7, "D", 7, "LEFT"))
    rules.append(("L", 7, "L", 8, "RIGHT"))
    
    rules.append(("A", 8, "A", 8, "RIGHT"))
    rules.append(("B", 8, "B", 8, "RIGHT"))
    rules.append(("C", 8, "C", 8, "RIGHT"))
    rules.append(("D", 8, "D", 8, "RIGHT"))
    rules.append(("0", 8, "A", 3, "RIGHT")) 
    rules.append(("1", 8, "B", 4, "RIGHT")) 
    rules.append(("R", 8, "R", 9, "LEFT")) 
    
    rules.append(("A", 9, "A", 9, "LEFT"))
    rules.append(("B", 9, "B", 9, "LEFT"))
    rules.append(("C", 9, "C", 9, "LEFT"))
    rules.append(("D", 9, "D", 9, "LEFT"))
    rules.append(("0", 9, "0", 10, "LEFT")) 
    rules.append(("1", 9, "1", 10, "LEFT")) 
    rules.append(("L", 9, "L", 11, "RIGHT")) 
    

    rules.append(("L", 10, "L", 10, "REJECT"))
    

    rules.append(("L", 11, "L", 11, "ACCEPT"))
    

    rules.append(("R", 2, "R", 10, "REJECT")) 
    
    return rules

if __name__ == "__main__":
    rules = create_rules()
    
    print(calculate("00", rules))      # True
    print(calculate("001001", rules))  # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules))      # False
    print(calculate("00100", rules))   # False
    print(calculate("10111101", rules)) # False