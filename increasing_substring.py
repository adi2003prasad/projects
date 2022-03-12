class increasing_substring():
    def __init__(self) -> None:
        major_lis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        m_dict_with_indices = {}
        for x in range(len(major_lis)):
            m_dict_with_indices[major_lis[x]
                                ] = m_dict_with_indices.get(major_lis[x], x)
        self.major_dict_indices = m_dict_with_indices

    def checker(self, number_terms, word):
        current_counter = 1
        lis_counters = []
        for x in range(number_terms):
            if(x == 0):
                current_counter = 1
            if(x > 0):
                if(self.major_dict_indices[word[x]] > self.major_dict_indices[word[x-1]]):
                    current_counter += 1
                else:
                    current_counter = 1
            lis_counters.append(current_counter)
        return lis_counters


ini = int(input(""))
list_all_test_cases = []
for a in range(ini):
    our_class = increasing_substring()
    num = int(input(""))
    string_needed = input("")
    answer = our_class.checker(num, string_needed)
    list_all_test_cases.append(answer)

# the last part output
for x in range(len(list_all_test_cases)):
    print("Case #"+str(x+1)+":", end="")
    for y in list_all_test_cases[x]:
        print(" {}".format(y), end="")
    print()
