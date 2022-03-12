class house():
    def __init__(self, no_of_houses, budget):
        self.no_of_houses = no_of_houses
        self.budget = budget
    def house_cost_assigner(self):
        costs_houses = []
        cost_a_j = input("").split()
        i = 0
        while(i<self.no_of_houses):
            costs_houses.append(int(cost_a_j[i]))
            i+=1
            # costs_houses.append(cost_a_j)
        costs_houses.sort()
        self.costs_houses = costs_houses
    def calculation_houses(self):
        max_houses = 0
        spendings = 0
        if(self.costs_houses[0]<self.budget):
            while(spendings<=self.budget):
                if((spendings+self.costs_houses[max_houses])>self.budget):
                    return max_houses
                else:
                    spendings+=self.costs_houses[max_houses]
                    max_houses+=1
            return max_houses
        else:
            return max_houses
    

a = int(input(""))
answers = []
for x in range(a):
    n_and_b = input("").split()
    allocator = house(int(n_and_b[0]), int(n_and_b[1]))
    allocator.house_cost_assigner()
    answers.append(allocator.calculation_houses())

for y in range(len(answers)):
    print("Case #"+str(y+1)+": "+ str(answers[y]))