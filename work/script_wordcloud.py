from lxml import etree
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from utils import extract_text
import sys

input_name = sys.argv[1]

path_to_file = '/CursoOpenScience/work/output/'+input_name[:len(input_name)-4]+'.grobid.tei.xml'
tree = etree.parse(path_to_file)

root = tree.getroot()


abstract_text = ''
for sections in root[0][2]:
    abstract_text += extract_text(sections)
    abstract_text += '\n'


dict = {}
string = ""
for char in abstract_text:
    if (not char.isspace() or char not in '.;,_ \n()\""'):
        string += char
    else:
        if len(string) != 0:
            if string in dict:
                dict[string] += 1
            else:
                dict[string] = 1
            string = ""


# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

