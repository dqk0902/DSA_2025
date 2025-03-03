class RepeatList:
    def __init__(self):
        self.numbers = []
        self.unique_numbers = set()
        self.has_repeat = False

    def append(self, number):
        self.numbers.append(number)
        if number in self.unique_numbers:
            self.has_repeat = True
        else:
            self.unique_numbers.add(number)

    def repeat(self):
        return self.has_repeat

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True