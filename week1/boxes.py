def min_count(product_count, box_size):
    if product_count % box_size == 0:
        return product_count // box_size
    else:
        return product_count // box_size + 1

if __name__ == "__main__":
    print(min_count(10, 3))  # Expected: 4
    print(min_count(10, 4))  # Expected: 3
    print(min_count(100, 1))  # Expected: 100
    print(min_count(100, 100))  # Expected: 1
    print(min_count(100, 99))  # Expected: 2
    print(min_count(5, 5))  # Expected: 1
    print(min_count(5, 6))  # Expected: 1