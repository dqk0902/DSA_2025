import math
def count_numbers(a, b):
   def generate_numbers(n):
        if n > b:
            return 0
        if n >= a:
            count = 1
        else:
            count = 0
    
        count += generate_numbers(n * 10 + 2)
        count += generate_numbers(n * 10 + 5)

        return count
   
   return generate_numbers(0)


if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512