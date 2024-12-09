def create(t, x):
    newList = []
    for i in t:
        newList.append(i+x)
    
    return newList

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]