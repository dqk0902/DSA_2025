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

def create_rules():
    rules = []
    
    rules.append(("L", 1, "L", 2, "RIGHT"))
    
    rules.append(("0", 2, "A", 3, "RIGHT"))
    rules.append(("1", 2, "B", 3, "RIGHT"))
    
    rules.append(("0", 3, "0", 3, "RIGHT"))
    rules.append(("1", 3, "1", 3, "RIGHT"))
    
    rules.append(("R", 3, "R", 4, "LEFT"))
    
    rules.append(("A", 4, "A", 4, "LEFT"))
    rules.append(("B", 4, "B", 4, "LEFT"))
    
    rules.append(("0", 4, "M", 5, "LEFT"))
    rules.append(("1", 4, "N", 5, "LEFT"))
    
    rules.append(("0", 5, "0", 5, "LEFT"))
    rules.append(("1", 5, "1", 5, "LEFT"))
    rules.append(("A", 5, "A", 5, "LEFT"))
    rules.append(("B", 5, "B", 5, "LEFT"))
    rules.append(("L", 5, "L", 6, "RIGHT"))
    
    rules.append(("L", 6, "L", 7, "RIGHT"))
    
    rules.append(("A", 7, "A", 8, "RIGHT"))
    rules.append(("B", 7, "B", 9, "RIGHT"))
    
    rules.append(("A", 8, "A", 8, "RIGHT"))
    rules.append(("B", 8, "B", 8, "RIGHT"))
    rules.append(("A", 9, "A", 9, "RIGHT"))
    rules.append(("B", 9, "B", 9, "RIGHT"))
    
    rules.append(("M", 8, "M", 10, "RIGHT"))
    rules.append(("N", 8, "N", 10, "RIGHT"))
    rules.append(("M", 9, "M", 11, "RIGHT"))
    rules.append(("N", 9, "N", 11, "RIGHT"))
    
    rules.append(("0", 10, "C", 12, "LEFT"))
    rules.append(("1", 11, "D", 12, "LEFT"))
    
    rules.append(("1", 10, "1", 20, "REJECT"))
    rules.append(("0", 11, "0", 20, "REJECT"))
    
    rules.append(("C", 12, "C", 12, "LEFT"))
    rules.append(("D", 12, "D", 12, "LEFT"))
    
    rules.append(("M", 12, "M", 12, "LEFT"))
    rules.append(("N", 12, "N", 12, "LEFT"))
    
    rules.append(("A", 12, "A", 12, "LEFT"))
    rules.append(("B", 12, "B", 12, "LEFT"))
    
    rules.append(("L", 12, "L", 6, "RIGHT"))
    
    rules.append(("0", 7, "0", 13, "RIGHT"))
    rules.append(("1", 7, "1", 13, "RIGHT"))
    
    rules.append(("0", 13, "0", 13, "RIGHT"))
    rules.append(("1", 13, "1", 13, "RIGHT"))
    
    rules.append(("M", 13, "M", 14, "RIGHT"))
    rules.append(("N", 13, "N", 14, "RIGHT"))
    
    rules.append(("0", 14, "0", 20, "REJECT"))
    rules.append(("1", 14, "1", 20, "REJECT"))
    
    rules.append(("C", 14, "C", 14, "RIGHT"))
    rules.append(("D", 14, "D", 14, "RIGHT"))
    
    rules.append(("R", 14, "R", 15, "ACCEPT"))
    
    rules.append(("R", 20, "R", 20, "REJECT"))
    
    return rules

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules))
    print(calculate("001001", rules))
    print(calculate("10111011", rules))
    print(calculate("01", rules))
    print(calculate("00100", rules))
    print(calculate("10111101", rules))