def create_string(pages):
    unique_pages = sorted(set(pages))
    
    ranges = []
    start = end = unique_pages[0]

    for page in unique_pages[1:]:
        if page == end + 1:
            end = page
        else:
            ranges.append((start, end))
            start = end = page

    ranges.append((start, end))

    result = []
    for start, end in ranges:
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")

    return ",".join(result)

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]