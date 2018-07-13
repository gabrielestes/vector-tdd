class Vector:
    def __init__(self, nums):
        self.nums = nums
        self.dims = len(self.nums)

    def norm(self):
        return sum([num**2 for num in self.nums])**0.5