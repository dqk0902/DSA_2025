from collections import defaultdict

class DistanceTracker:
    def __init__(self):
        self.positions = defaultdict(list)
        self.sums = defaultdict(int)
        self.totals = defaultdict(int)
        self.index = 0

    def append(self, number):
        if number in self.positions:
            last_pos = self.positions[number][-1]
            distance = self.index - last_pos
            self.sums[number] += distance * len(self.positions[number])
            self.totals[number] += self.sums[number]
        self.positions[number].append(self.index)
        self.index += 1

    def sum(self, number):
        return self.totals[number]

if __name__ == "__main__":
    tracker = DistanceTracker()
    tracker.append(1)
    print(tracker.sum(1))  # 0
    tracker.append(1)
    print(tracker.sum(3))  # 0
    tracker.append(1)
    print(tracker.sum(1))  # 4
