def evaluate(data):
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        if i + 4 < n and data[i:i+4] == "add(" and i + 4 < n:
            j = i + 4
            paren_depth = 1
            while j < n and paren_depth > 0:
                if data[j] == '(':
                    paren_depth += 1
                elif data[j] == ')':
                    paren_depth -= 1
                j += 1
            
            if paren_depth == 0: 
                expr = data[i:j]
                if is_valid_expression(expr):
                    args = expr[4:-1].split(',')
                    x, y = int(args[0]), int(args[1])
                    result.append(str(x + y))
                    i = j
                else:
                    result.append(data[i])
                    i += 1
            else:
                result.append(data[i])
                i += 1
        elif i + 4 < n and data[i:i+4] == "mul(" and i + 4 < n:
            j = i + 4
            paren_depth = 1
            while j < n and paren_depth > 0:
                if data[j] == '(':
                    paren_depth += 1
                elif data[j] == ')':
                    paren_depth -= 1
                j += 1
            
            if paren_depth == 0:  
                expr = data[i:j]
                if is_valid_expression(expr):
                    args = expr[4:-1].split(',')
                    x, y = int(args[0]), int(args[1])
                    result.append(str(x * y))
                    i = j
                else:
                    result.append(data[i])
                    i += 1
            else:
                result.append(data[i])
                i += 1
        else:
            result.append(data[i])
            i += 1
    
    return "".join(result)

def is_valid_expression(expr):
    if not (expr.startswith("add(") or expr.startswith("mul(")) or not expr.endswith(")"):
        return False
    
    content = expr[4:-1]
    
    parts = content.split(',')
    if len(parts) != 2:
        return False
    
    x, y = parts
    
    if not x or not y:
        return False
    
    if ' ' in x or ' ' in y or '.' in x or '.' in y or '-' in x or '-' in y:
        return False
    
    if (len(x) > 1 and x[0] == '0') or (len(y) > 1 and y[0] == '0'):
        return False
    
    if not x.isdigit() or not y.isdigit():
        return False
    
    if int(x) <= 0 or int(y) <= 0:
        return False
    
    return True

if __name__ == "__main__":
    print(evaluate("add(1,2)"))  # 3
    print(evaluate("aybabtu"))  # aybabtu
    print(evaluate("mul(6,7),mul(7,191)"))  # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)"))  # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)"))  # mul()mul(13)mul(0,1)

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result))  # 200000
    print(result[:20])  # 42424242424242424242