def calculate(input, rules):
    string = "L" + input + "R"

    tape = list(string)
    
    state = 1
    position = 0
    
    rule_dict = {}
    for symbol, current_state, new_symbol, new_state, action in rules:
        rule_dict[(symbol, current_state)] = (new_symbol, new_state, action)
    
    for _ in range(1000):
        if position < 0 or position >= len(tape):
            return False
        
        current_symbol = tape[position]
        
        if (current_symbol, state) not in rule_dict:
            return False
        
        new_symbol, new_state, action = rule_dict[(current_symbol, state)]
        tape[position] = new_symbol
        state = new_state
        
        if action == "LEFT":
            position -= 1
        elif action == "RIGHT":
            position += 1
        elif action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False
    
    return False

if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules))  # False
    print(calculate("00", rules))  # False
    print(calculate("01", rules))  # True
    print(calculate("0110", rules))  # True
    print(calculate("0101", rules))  # True
    print(calculate("1000", rules))  # False
    print(calculate("00110101", rules))  # True
    print(calculate("00111101", rules))  # False