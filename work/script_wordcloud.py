from lxml import etree
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from utils import extract_text



tree = etree.parse('./output/exemple_pdf4.grobid.tei.xml')

root = tree.getroot()




total_text = ''
for sections in root[2][0]:
    total_text += extract_text(sections)
    total_text += '\n'

#print(total_text)

dict = {}
string = ""
for char in total_text:
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

