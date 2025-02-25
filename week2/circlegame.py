def find_order(n):
    players = list(range(1, n + 1))
    
    leaving_order = []
    
    current_index = 0 # pointer
    
    while players:
        current_index = (current_index + 1) % len(players)
        
        leaving_order.append(players.pop(current_index))

        if not players:
            break
    
    return leaving_order

if __name__ == "__main__":
    print(find_order(1))  # [1]
    print(find_order(2))  # [2, 1]
    print(find_order(3))  # [2, 1, 3]
    print(find_order(7))  # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:])  # [52545, 85313, 36161, 3393, 68929]