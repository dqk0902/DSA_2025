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
    
    # Start state: Move right to the first symbol
    rules.append(("L", 1, "L", 2, "RIGHT"))
    
    # State 2: Read and mark the first symbol
    rules.append(("0", 2, "X", 3, "RIGHT"))  # Mark 0 as X and move to state 3
    rules.append(("1", 2, "Y", 4, "RIGHT"))  # Mark 1 as Y and move to state 4
    rules.append(("R", 2, "R", 8, "ACCEPT"))  # If no symbols, accept (empty string)
    
    # State 3: Process 0s (move right until end)
    rules.append(("0", 3, "0", 3, "RIGHT"))
    rules.append(("1", 3, "1", 3, "RIGHT"))
    rules.append(("R", 3, "R", 5, "LEFT"))  # At end, move left to mark a 0
    
    # State 4: Process 1s (move right until end)
    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("1", 4, "1", 4, "RIGHT"))
    rules.append(("R", 4, "R", 6, "LEFT"))  # At end, move left to mark a 1
    
    # State 5: Mark the rightmost 0 as X
    rules.append(("0", 5, "X", 7, "LEFT"))  # Mark 0 as X and move left
    rules.append(("1", 5, "1", 5, "LEFT"))  # Skip 1s
    rules.append(("X", 5, "X", 5, "LEFT"))  # Skip Xs
    rules.append(("Y", 5, "Y", 5, "LEFT"))  # Skip Ys
    
    # State 6: Mark the rightmost 1 as Y
    rules.append(("1", 6, "Y", 7, "LEFT"))  # Mark 1 as Y and move left
    rules.append(("0", 6, "0", 6, "LEFT"))  # Skip 0s
    rules.append(("X", 6, "X", 6, "LEFT"))  # Skip Xs
    rules.append(("Y", 6, "Y", 6, "LEFT"))  # Skip Ys
    
    # State 7: Move left to find the next unmarked symbol
    rules.append(("0", 7, "0", 7, "LEFT"))
    rules.append(("1", 7, "1", 7, "LEFT"))
    rules.append(("X", 7, "X", 7, "LEFT"))
    rules.append(("Y", 7, "Y", 7, "LEFT"))
    rules.append(("L", 7, "L", 2, "RIGHT"))  # At start, move right to process next symbol
    
    # State 8: Accept state (no rules needed)
    
    return rules
if __name__ == "__main__":
    rules = create_rules()
    
    print(calculate("00", rules))      # True
    print(calculate("001001", rules))  # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules))      # False
    print(calculate("00100", rules))   # False
    print(calculate("10111101", rules)) # False