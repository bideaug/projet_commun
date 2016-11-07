#! /usr/bin/pyhton2.7

import numpy as np
import matplotlib.pyplot as plt

fichier = open("dic.txt","r")

line = fichier.read()
line = line.lower()
word = line.split()

print word
