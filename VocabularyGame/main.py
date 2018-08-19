from optparse import OptionParser

from classes.gameMaster import GameMaster
from classes.levelManager import LevelManager
from classes.question import Question
from classes.wordLoader import WordLoader
from classes.displayer import Displayer
from classes.converter import Converter

parser = OptionParser()
parser.add_option("-g", "--graphical", dest="isGraphical", default=False, action="store_true", help="Display the graphical interface")
parser.add_option("-c", "--convert", dest="convert", default=False, action="store_true",help="Convert data from source to dest")
parser.add_option("-s", "--src", dest="srcFile", default=None, help="Path to source")
parser.add_option("-d", "--dest", dest="destFile", default=None, help="Path to destination")
(options, args) = parser.parse_args()

def main(options, args):
    if parser.values.isGraphical :
        d = Displayer()
    if parser.values.convert :
        if parser.values.srcFile != None and \
        parser.values.destFile != None :
            c = Converter(parser.values.srcFile, parser.values.destFile)

if __name__ == '__main__':
    main(options, args)
