class C:
    def __init__(self, data):
        self.data = data
    def m1(self, s, n):
        self.data[s] = n
    def m2(self, s):
        total = 0
        for sector in s:
            if sector in self.data:  
                total += self.data[sector] 
            else:
                total += 0 
        return total
    
C({"A":120,"D":150,"G":90,"K":110})
C.m1("G",130)
C.m2("GD") 
C.m2("KEJ") 