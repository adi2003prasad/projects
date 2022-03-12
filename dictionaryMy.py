import string

from numpy import power


class search():
    def __init__(self, list_i, word, power):
        self.list_i = list_i
        self.word = word
        alphaword = string.ascii_uppercase
        alphaslower = string.ascii_lowercase
        self.alphalowerli = list(alphaslower)
        self.alphas = list(alphaword)
        self.power = power

    def helper(self, point, to_find, indice, word, power):
        res = self.binarySearchIni(
            self.list_i[point-(2*power):point-power], to_find, self.alphalowerli, indice)
        if res:
            return self.complexHandler(res, word[1:], indice+1, power)
        else:
            res = self.binarySearchIni(
                self.list_i[point+power:point+(2*power)], to_find, self.alphalowerli, indice)
            if res:
                return self.complexHandler(res, word[1:], indice+1, power)
            else:
                return self.helper(point, to_find, indice, word, power*2)

    def complexHandler(self, point, word, indice, power):
        print(word[0])
        if len(word) == 1:
            res = self.binarySearchIni(
                self.list_i[point-power:point+power], word[0], self.alphalowerli, indice)
            print(res)
            return(res)
        else:
            res = self.binarySearchIni(
                self.list_i[point-power:point+power], word[0], self.alphalowerli, indice)
            if res:
                print(res)
                return self.complexHandler(res, word[1:], indice+1, power)
            else:
                return self.helper(res, word[0], indice, word, power)

    def handler(self):
        res = self.binarySearchIni(self.list_i, self.word[0], self.alphas, 1)
        print(res)
        return self.complexHandler(res, word[1:], 2, self.power)

    def binarySearchIni(self, list_i, to_find, alphaslist, index):
        length = len(list_i)
        if(length % 2 == 0):
            point = length//2
        else:
            point = (length+1)//2
        in_list = list_i[point][index]
        if (in_list == to_find):
            return point
        else:
            print("inlist", in_list)
            print("to find", to_find)
            if (alphaslist.index(in_list) < alphaslist.index(to_find)):
                return self.binarySearchIni(list_i[point:], to_find, alphaslist, index)
            else:
                return self.binarySearchIni(list_i[0:point], to_find, alphaslist, index)


file = "dictionary.txt"
handle = open(file)
data = handle.readlines()
while True:
    word = input("enter the word to search : ")
    if(word == "end"):
        break
    else:
        a = search(data, word, 500)
        a.handler()
