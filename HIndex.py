
def calculator(priorityQ, indexH):
    # print(priorityQ, indexH)
    score = 0
    for x in priorityQ:

        if(x >= indexH):
            score += 1
        else:
            pass
        if(score >= indexH):
            # print("win")
            return True
    return False


def prioritysorter(currentLst, priorityq, indexH):
    # print(indexH, "the check", currentLst)
    for x in currentLst:
        if(x > indexH):
            priorityq.append(x)
    # print(priorityq, "the created priority queue")
    return priorityq


def h_index(n, citations):
    ans = []
    # TODO: Complete the function to get the H-Index scores after each paper
    indexH = 1
    priorityQ = [citations[0]]
    a = max(citations)
    if(citations[0] >= indexH):
        ans.append(indexH)

    for x in range(1, n):

        priorityQ.append(citations[x])
        # print(priorityQ, "priority list")
        # print(citations[x])
        if(calculator(priorityQ, indexH)):
            # print(priorityQ, " priorityQueue ", indexH)

            priorityQ = prioritysorter(priorityQ, [], indexH)

            ans.append(indexH)
            indexH += 1
        else:
            priorityQ = prioritysorter(priorityQ, [], indexH)
            ans.append(indexH-1)

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        citations = input().split()  # The number of citations for each paper
        citInt = [int(xi) for xi in citations]
        h_index_scores = h_index(n, citInt)
        print("Case #" + str(test_case) + ": " +
              ' '.join(map(str, h_index_scores)))
