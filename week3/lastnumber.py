def find(t):
    return sum(t) - len(t) + 1

if __name__ == "__main__":
    print(find([1,2,3,4])) # 7
    print(find([1,1,1])) # 1
    print(find([5,1,1,7,9,1,2])) # 20