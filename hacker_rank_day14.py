class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.__elements.sort();
        diff = self.__elements[len(self.__elements)-1] - self.__elements[0]
        self.maximumDifference=diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)