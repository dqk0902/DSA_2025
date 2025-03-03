from collections import defaultdict

class OccurrenceTracker:
    def __init__(self):
        self.number_counts = defaultdict(int)
        self.count_occurrences = defaultdict(int)
        self.distinct_counts = 0

    def append(self, number):
        old_count = self.number_counts[number]
        new_count = old_count + 1
        
        self.number_counts[number] = new_count
        
        self.count_occurrences[old_count] -= 1
        if self.count_occurrences[old_count] == 0:
            del self.count_occurrences[old_count]
            if old_count > 0:
                self.distinct_counts -= 1
        
        self.count_occurrences[new_count] += 1
        if self.count_occurrences[new_count] == 1:
            self.distinct_counts += 1

    def count(self):
        return self.distinct_counts

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3
