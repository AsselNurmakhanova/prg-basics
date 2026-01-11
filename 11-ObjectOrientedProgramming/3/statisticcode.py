class Statistics:
    def __init__(self, set):
        self.set = set
    def show(self):
        for num in self.set:
            print(num, end=" ")
    def greatest(self):
        greatest = self.set[0]
        for num in self.set:
            if num > greatest:
                greatest = num
        return greatest
    def smallest(self):
        smallest = self.set[0]
        for num in self.set:
            if num < smallest:
                smallest = num
        return smallest
    def mean(self):
        total = 0
        for num in self.set:
            total += num
        return total / len(self.set)
    def median(self):
        sorted_set = sorted(self.set)
        n = len(sorted_set)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_set[mid - 1] + sorted_set[mid]) / 2
        else:
            return sorted_set[mid]