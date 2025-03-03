class DataAnalyzer:
    def __init__(self):
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xx = 0
        self.sum_xy = 0
        self.sum_yy = 0
        self.n = 0

    def add_point(self, x, y):
        self.sum_x += x
        self.sum_y += y
        self.sum_xx += x * x
        self.sum_xy += x * y
        self.sum_yy += y * y
        self.n += 1

    def calculate_error(self, a, b):
        return (self.sum_yy + 
                (a*a * self.sum_xx) + 
                (self.n * b*b) + 
                (2*a*b * self.sum_x) - 
                (2*a * self.sum_xy) - 
                (2*b * self.sum_y))

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0))  # 5
    print(analyzer.calculate_error(1, -1))  # 2
    print(analyzer.calculate_error(3, 2))  # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0))  # 9
    print(analyzer.calculate_error(1, -1))  # 3
    print(analyzer.calculate_error(3, 2))  # 437

    # Efficiency test
    analyzer = DataAnalyzer()
    total = 0
    for i in range(10**5):
        analyzer.add_point(i, i % 100)
        total += analyzer.calculate_error(i % 97, i % 101)
    print(total)  # 25745448974503313754828
