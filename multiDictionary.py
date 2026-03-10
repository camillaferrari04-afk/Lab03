from datetime import datetime

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language:str) ->list:
        if language.lower() == "english":
            path= "resources/English.txt"
        elif language.lower() == "italian":
            path = "resources/Italian.txt"
        elif language.lower() == "spanish":
            path = "resources/Spanish.txt"
        else:
            print("Lingua non valida")
            return None
        dictionary = d.Dictionary()
        dictionary.loadDictionary(path)
        return dictionary.printAll()


    def searchWordIn(self, words:list, language:str) ->tuple:
        richlist=[]
        dictionary=self.printDic(language)
        time1=datetime.now()
        for word in words:
            richword= rw.RichWord(word)
            if word in dictionary:
                richword.corretta=True
            else:
                richword.corretta=False
            richlist.append(richword)
        time2=datetime.now()
        totaltime=time2-time1
        return richlist, totaltime

    def searchWordLinear(self, words:list, language:str) ->tuple:
        richlist=[]
        dictionary=self.printDic(language)
        time1=datetime.now()
        for word in words:
            richword = rw.RichWord(word)
            richword.corretta = False
            for w in dictionary:
                if word==w:
                    richword.corretta=True
                    break
            richlist.append(richword)
        time2=datetime.now()
        totaltime=time2-time1
        return richlist, totaltime

    def searchWordDichotomic(self, words:list, language:str) ->list:
        richlist=[]
        dictionary=self.printDic(language)
        time1 = datetime.now()
        for word in words:
            richword= rw.RichWord(word)
            richword.corretta = False
            start=0
            end=len(dictionary)-1
            while start<=end:
                if word==dictionary[(start+end)//2]:
                    richword.corretta=True
                    break
                else:
                    if word<dictionary[(start+end)//2]:
                        end=(start+end)//2-1
                    else:
                        start=(start+end)//2+1
            richlist.append(richword)
        time2 = datetime.now()
        totaltime = time2 - time1
        return richlist, totaltime


