import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, text:str, language:str):
        words=self.cleanSentence(text)
        multidic= md.MultiDictionary()
        (richlist,totaltime)=multidic.searchWordIn(words, language)
        print("______________________________")
        print("Using In")
        for i in richlist:
            if not i.corretta:
                print(i)
        print("Time Elapsed",totaltime)

        (richlist, totaltime) = multidic.searchWordLinear(words, language)
        print("______________________________")
        print("Using Linear search")
        for i in richlist:
            if not i.corretta:
                print(i)
        print("Time Elapsed",totaltime)

        (richlist, totaltime) = multidic.searchWordDichotomic(words, language)
        print("______________________________\n")
        print("Using Dichotomic search")
        for i in richlist:
            if not i.corretta:
                print(i)
        print("Time Elapsed", totaltime)
        print("______________________________\n")

    def cleanSentence(self, txtIn:str) ->list:
        chars = "\\`*_{}[]()>#+-.!$?'%^;,=_~"
        for c in chars:
            txtIn = txtIn.replace(c, "")
        words = txtIn.lower().split()
        return words

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    pass