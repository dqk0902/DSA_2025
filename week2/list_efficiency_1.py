import time

def test_list_efficiency(n):
    list = []

    start_add_time = time.time()
    for i in range(1, n+1):
        list.append(i)
    add_time = time.time() - start_add_time

    start_delete_time =  time.time()
    for _ in range(n):
        list.pop()
    delete_time = time.time() - start_delete_time

    print(f"Time taken to append {n} elements: {add_time:.3f} seconds")
    print(f"Time taken to delete {n} elements: {delete_time:.3f} seconds")

if __name__ == "__main__":
    n = 10**5
    test_list_efficiency(n)