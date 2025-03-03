class PermutationTracker:
    def __init__(self):
        self.numbers = set()
        self.max_number = 0
        self.count = 0

    def append(self, number):
        self.count += 1
        self.numbers.add(number)
        self.max_number = max(self.max_number, number)

    def check(self):
        return len(self.numbers) == self.count == self.max_number

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(1)
    print(tracker.check())  # True

    tracker.append(4)
    print(tracker.check())  # False

    tracker.append(3)
    print(tracker.check())  # True

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(5)
    print(tracker.check())  # False