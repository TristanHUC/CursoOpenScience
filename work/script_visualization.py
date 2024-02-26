from lxml import etree
from utils import extract_text
import os
from matplotlib import pyplot as plt

directory = "./output"

data = {}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    tree = etree.parse(file_path)

    root = tree.getroot()
    nb_figure = 0


    text = extract_text(root)
    word = ""
    next_word = ""

    #Iterate on the whole text to find the word 'figure' or 'fig' and capture the maximum number behind
    for i, char in enumerate(text):

        #current word
        if (not char.isspace() and char not in '.;,_\n()\""'):
            word += char
        else:
            #find the number of space to pass
            s = 1
            for space in text[i+1:]:
                if space.isspace():
                    s += 1
                else :
                    break

            #if the word is good, look for the next word behind
            if word.lower() in ('fig', 'figure'):
                for char2 in text[i+s:]:

                    #check if the word behind is ended and if not check if it's a digit
                    if (not char2.isspace() and char2 not in '.;,\n()\""'):
                        if char2.isdigit():
                            next_word += char2
                        else :
                            break
                    else :
                        #when next word is over, compare it to the current nb of figure known
                        if int(next_word) > nb_figure:
                            nb_figure = int(next_word)
                            break
                        else :
                            break
            word = ""
            next_word = ""

    reduced_filename = filename[10:15]
    data[reduced_filename] = nb_figure

    #trying to do it with figures only but some specific cases cause problems
    #nb_figure = 0
    #for sections in root[2][0]:
    #    if sections.tag.endswith('figure'):
    #        #print(sections[0].text)
    #        if sections[0].text[0:3] == 'Fig':
    #            nb_figure+=1

plt.bar(list(data.keys()), list(data.values()))
plt.show()