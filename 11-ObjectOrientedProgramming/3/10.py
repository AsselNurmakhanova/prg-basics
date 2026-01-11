class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def m(self, n):
        self.n = n
        total = 0
        for x,y in self.coordinates:
                if x > 0 and y > 0:
                    total += 1
        if total == n:
            return True
        else:
            return False

c = C([[2,3],[1,8],[-6,4],[3,-7]])
print(c.m(3))