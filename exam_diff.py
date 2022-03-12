class exam():
    def __init__(self, n, m) -> None:
        self.number_of_sets = n
        self.number_of_students = m
    def set_maker(self):
        self.sets = []
        for x in range(self.number_of_sets):
            inputs = input("").split()
            for y in range(int(inputs[0]), int(inputs[1])+1):
                if(y not in self.sets):
                    self.sets.append(y)
                else:
                    continue
        self.sets.sort()
    def bisection_finder(self, number_to_find):
        def helper(start, end, number, list):
            if(start==end):
                if(list[start]==number):
                    return list[start]
                else:
                    return False
            else:
                mid = (start+end)//2
                if(number==list[mid]):
                    return list[mid]
                else:
                    if(list[mid]>number):
                        # print(start, mid)
                        return(helper(start, mid, number, list))
                    else:
                        # print(mid, end)
                        return(helper(mid+1, end, number, list))
        problem = helper(0, len(self.sets), number_to_find, self.sets)
        if(problem):
            self.sets.pop(self.sets.index(problem))
            return problem
        else:
            a = self.approximator(number_to_find)
            self.sets.pop(self.sets.index(a))
            return(a)

    def approximator(self, number):
        self.differences = []
        for x in self.sets:
            a = abs(number-x)
            if(len(self.differences)>=1):
                b = min(self.differences)
                if(a>b):
                    break
                else:
                    self.differences.append(a)
            else:
                self.differences.append(a)
        a = min(self.differences)
        # print(a)
        return self.sets[self.differences.index(a)]


    def student_picker(self):
        
        self.students_skills = []
        a = input("").split()
        for x in a:
            self.students_skills.append(int(x))
        

    def picker(self):
        self.answers = []
        for x in self.students_skills:
            self.answers.append(self.bisection_finder(x))
        return self.answers
    

input_1 = int(input(""))
answers = []
while input_1>0:
    inputs = input("").split()
    test = exam(int(inputs[0]), int(inputs[1]))
    test.set_maker()
    # print(test.sets)
    test.student_picker()
    answers.append(test.picker())
    input_1-=1

for y in answers:
    print("Case #"+str(answers.index(y)+1)+":" , end=" ")
    [print(x, end=" ") for x in y]
    print()