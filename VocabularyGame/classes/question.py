from random import randint
from .word import Word
from .wordLoader import WordLoader


class Question:
    def __init__(self, words, word = "", fromLang1ToLang2 = True):
        self.availableWords = words
        self.wordToFound = word if (word !=  "" ) else self.pickAWord()
        self.numberOfPossibleAnwsers = 4
        self.fromLang1ToLang2 = fromLang1ToLang2
        self.wrongAnwsers = []
        self.pickWords()
        self.shuffleWords = self.shuffle()

    def pickWords(self):
        if (self.wordToFound == ""):
            self.pickAWord()
        i = 1
        while (i <= self.numberOfPossibleAnwsers) :
            candidateWordToAppend = self.pickAWord()
            if (self.wordToFound != candidateWordToAppend and candidateWordToAppend not in self.wrongAnwsers) :
                self.wrongAnwsers.append(candidateWordToAppend)
                i += 1

    def getFullLanguageName(self, abreviateLanguageName):
        knownAbreviateLanguageNames = ["de", "fr"]
        if (abreviateLanguageName not in abreviateLanguageName):
            raise Error("Unknown language abreviation : " + abreviateLanguageName)
        return "french" if abreviateLanguageName == "fr" else "german"

    def generateHeader(self):
        str = "The word "
        if (self.fromLang1ToLang2) :
            str =+ self.wordToFound.getSpelling(0)
            str += " in "
            str += self.wordToFound.getVersion(0)
            str += " is "
            str += " in "
            str += self.wordToFound.getVersion(1)
        else :
            str =+ self.wordToFound.getSpelling(1)



    def generateQuestion(self):
        self.generateHeader()

    def pickAWord(self):
        return self.availableWords[randint(0, len(self.availableWords)-1)]

    def __str__(self) :
        str = "The word to find is : " \
        + self.wordToFound.__str__() \
        + " et les faux mots sont : " \
        + self.wrongAnwsers[0].__str__() \
        + self.wrongAnwsers[1].__str__() \
        + self.wrongAnwsers[2].__str__()
        return str

    def shuffle(self):
        words = self.wrongAnwsers.copy()
        words.append(self.wordToFound)
        shuffledWords = []
        i = 0
        while (i < self.numberOfPossibleAnwsers) :
            index = randint(0, len(words)-1)
            wordToMix = words.pop(index)
            shuffledWords.append(wordToMix)
            i += 1
        return shuffledWords

    def getShuffleWords(self):
        if (len(self.shuffleWords) == 0 ) :
            self.shuffle()
        return self.shuffleWords



if __name__ == '__main__' :
    wl = WordLoader("../data/lvl1.json", "json")
    q = Question(wl.getWords())
