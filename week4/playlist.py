def count_parts(songs):
    # sliding window
    song_set = set()
    left = 0
    count = 0
    
    for right in range(len(songs)):
        while songs[right] in song_set:
            song_set.remove(songs[left])
            left += 1
        
        song_set.add(songs[right])
        count += right - left + 1
    
    return count

if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1]))  # 4
    print(count_parts([1, 2, 3, 4]))  # 10
    print(count_parts([1, 2, 1, 2]))  # 7
    print(count_parts([1, 2, 1, 3]))  # 8
    print(count_parts([1, 1, 2, 1]))  # 6
    
    songs = [1, 2] * 10**5
    print(count_parts(songs))  # 399999
    
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs))  # 15000050000