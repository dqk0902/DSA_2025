def count(t):
    def flat_list(l):
        if isinstance(l, list):
            temp = []
            for ele in l:
                temp.extend(flat_list(ele))
            return temp
        else:
            return [l]
    
    return len(flat_list(t))

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8