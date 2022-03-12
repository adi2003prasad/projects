

from ast import Return


class hex():
    def initializerState(self):
        hexBoard = []
        counter_data = {}
        for x in range(self.n):
            xi = input()
            hexBoard.append(xi)
            for xii in xi:
                counter_data[xii] = counter_data.get(xii, 0) + 1

        self.hexBoard = hexBoard
        self.boardData = counter_data

    def __init__(self, n):
        self.n = n
        self.alls = ['B', 'R', '.']
        self.initializerState()
        self.answers = []
        self.blueFinder()

    def Impossiblecaller(self):
        self.answers.append("Impossible")

    def BlueWinCaller(self):
        self.answers.append("Blue Wins")

    def RedWinCaller(self):
        self.answers.append("Red Wins")

    def Nobody(self):
        self.answers.append("Nobody Wins")

    def RedFinder(self):
        dataR = {}
        RwinCounter = 0
        for lines in self.hexBoard:
            for element in range(len(lines)):
                if(lines[element] == self.alls[1]):
                    dataR[element] = dataR.get(element, 0) + 1
        for x in dataR:
            if(dataR[x] == self.n):
                RwinCounter += 1

        if(RwinCounter > 1):
            return self.Impossiblecaller()
        elif(RwinCounter == 1):
            return self.RedWinCaller()
        else:
            self.Nobody()

    def moverForBlue(self, player, n):
        if(n == 0):
            path = 0
            currentlyCounting = False
            index = 0
            listToCall = self.hexBoard
        elif(n == 1):
            path = 0
            currentlyCounting = False
            index = 0
            listToCall = []
            dupList = self.hexBoard
            dupList.reverse()
            for x in dupList:
                listToCall.append(x[::-1])
            # print(listToCall)
        else:
            return 0
        # dic = {0:"from up to down ", 1:"from down to up"}
        for x in listToCall:
            if(currentlyCounting == False):
                # print(x[0] == player, x[0])
                if(x[0] == player) and (currentlyCounting == False):
                    for alphas in range(len(x)):
                        print(x[alphas], x[alphas] == player,
                              currentlyCounting, alphas, index)
                        #       currentlyCounting == False, ALLPJ, index)
                        if(x[alphas] == player) and (currentlyCounting == False):
                            currentlyCounting = True
                            index = alphas
                        elif(currentlyCounting == True) and (alphas == player) and (alphas-index == 1):
                            path += 1
                            index = alphas
                        elif(currentlyCounting != True):
                            continue
                        else:
                            break

            else:
                if(x[index] == player) and (currentlyCounting == True):
                    path += 1
                    surr = x[index+1:]
                    backlog = 0
                    for a in range(len(surr)):
                        if(currentlyCounting == True) and (a == 0) and (surr[a] == player):
                            path += 1
                            index += 1
                            backlog = a
                        elif(currentlyCounting == True) and (surr[a] == player) and (a-backlog == 1):
                            index += 1
                            Lindex += 1
                            path += 1
                            backlog = a
                        else:
                            break
                    continue

        print(index)
        if(index == ((self.n)-1)):
            return self.BlueWinCaller()
        else:
            if(n == 0):
                return self.moverForBlue(player, n+1)
            else:
                return 0

    def blueFinder(self):
        if(abs(self.boardData.get("B", 0)-self.boardData.get("R", 0)) > 1):
            return self.Impossiblecaller()
        bWincounter = 0
        for x in self.hexBoard:
            if(self.alls[1] in x):
                continue
            elif(self.alls[2] in x):
                continue
            else:
                bWincounter += 1
        if(bWincounter > 1):
            return self.Impossiblecaller()
        elif(bWincounter == 1):
            return self.BlueWinCaller()
        # NOW WE HAVE TO FIND IF THE BLUE IS WINNING BY CONNECTING NON VERTICALLY
        else:
            print(self.alls[0], "player")
            self.floodFill(self.alls[0])
            # if(self.moverForBlue(self.alls[0], 0) == 0):
            #     return self.RedFinder()

    def output(self):
        return self.answers[0]

    def floodFill(self, player):
        currentlyCounting = False
        Cindex = 0
        for x in range(len(self.hexBoard)):
            if(Cindex == self.n-1):
                return self.BlueWinCaller()
            else:
                pass
            line_found = False
            for a in range(x):
                z = self.hexBoard[x][a]
                if(z == player) and (currentlyCounting == False) and (line_found == False) and (a == 0):
                    currentlyCounting = True
                    line_found = True
                    Cindex = a
                    if(Cindex == self.n-1):
                        return self.BlueWinCaller()
                    continue
                elif(z == player) and (currentlyCounting == True) and (a-Cindex == 1) and (line_found == True):
                    Cindex = a
                    if(Cindex == self.n-1):
                        return self.BlueWinCaller()
                    continue
                elif(z != player) and (currentlyCounting == True) and (line_found == True):
                    break
                elif(z != player) and (currentlyCounting == True) and (line_found == False):
                    continue
                elif(z == player) and (currentlyCounting == True) and (Cindex-a == 1) and (line_found == False):
                    Cindex = a

                    line_found = True
                    if(Cindex == self.n-1):
                        return self.BlueWinCaller()
                    continue
                elif(z == player) and (currentlyCounting == True) and (line_found == False):
                    line_found == True
                    Cindex == a
                    if(Cindex == self.n-1):
                        return self.BlueWinCaller()
        return self.Nobody()


t = int(input())
allAnswers = []
for x in range(t):
    n = int(input())
    obj = hex(n)
    allAnswers.append(obj.output())

for x in range(len(allAnswers)):
    print("Case #"+str(x+1)+": " + allAnswers[x])
