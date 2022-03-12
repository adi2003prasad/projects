class candy_distributor():
    def __init__(self, numberOfChildren, numberOfBags):
        all_candies = 0
        i = input("").split()  # the number of candies in each bag
        for xi in i:
            all_candies += int(xi)
        self.allCandies = all_candies
        self.m = numberOfChildren
        self.n = numberOfBags

    def distributor(self):
        max_candies = self.allCandies//self.m
        used_candies = max_candies*self.m
        left_candies = self.allCandies-used_candies
        self.candiesLeft = left_candies

    def handler(self):
        self.distributor()
        return self.candiesLeft


ans = []
i = int(input(""))
for x in range(i):
    a = input().split()
    obj = candy_distributor(int(a[1]), int(a[0]))
    ans.append(obj.handler())

for x in range(len(ans)):
    print("Case #"+str(x+1)+": "+str(ans[x]))
