from lxml import etree
from utils import extract_text, look_for_links

link_list = []

tree = etree.parse('./output/exemple_pdf10.grobid.tei.xml')

root = tree.getroot()

#retrieve link out of the text
l = look_for_links(root)


#extraire tout le texte
total_text = ''
total_text = extract_text(root)

#retrieve link from the text
string = ""
for char in total_text:
    if (not char.isspace() or char not in ';,_ \n()\""'):
        string += char
    else:
        if string[0:4] == 'http':
            l.append(string)
        string = ""

print(l)

