class Word:
    def __init__(self, wordInFirstLang, wordInSecondLang, inflections="", plural="",comment="", lang1="de", lang2="fr"):
        if (wordInFirstLang == "" or wordInSecondLang == ""):
            raise Exception("Cannot build a word from an empty data")
        self.version = {"0": str(lang1), "1": str(lang2)}
        self.spelling = {str(lang1): wordInFirstLang, str(lang2): wordInSecondLang}
        self.options = {"inflection" : inflections, "comment": comment, "plural": plural}
        self.availableOptions = ["inflection","comment","plural"]

    def __str__(self):
        res = "The word "
        res += self.spelling[self.version["0"]]
        res += " in "
        res += self.version["0"]
        res += " is "
        res += self.spelling[self.version["1"]]
        res += " in "
        res += self.version["1"]
        for opts in self.options.keys() :
            if (self.options[opts] != "") :
                res += ".\nThis word possesses the following " + str(opts) + " : " + self.options[opts]
        res += "\n"
        return res

    def setAnOption(self, optLabel, optValue):
        if (optLabel in self.availableOptions):
            self.options[optLabel] = optValue

    def __eq__(self, wordToCompare):
        if (not isinstance(wordToCompare, Word)):
            return False
        areEqual = self.version["0"] == wordToCompare.version["0"]
        areEqual = areEqual and self.version["1"] == wordToCompare.version["1"]
        areEqual = areEqual and self.spelling[self.version["0"]] == wordToCompare.spelling[self.version["0"]]
        areEqual = areEqual and self.spelling[self.version["1"]] == wordToCompare.spelling[self.version["1"]]
        for optLabel in self.availableOptions :
            areEqual = areEqual and self.options[optLabel] == wordToCompare.options[optLabel]
        return areEqual

    def getSpelling(self, version):
        return self.spelling[self.getVersion(version)]

    def getVersion(self, number):
        return self.version[str(number)]

if __name__ == '__main__':
    word = Word("stellen", "mettre", "[a i o]", "(e)", "debout")
    print(word)
    word.setAnOption("comment", "assis")
    print(word)
