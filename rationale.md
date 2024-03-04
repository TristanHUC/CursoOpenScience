# Introduction 
Due to the fact that grobid returns the same architecture for each pdf file, we can just apply the same browsing structure for any file.

# utils.py
This python module contains two functions : 
- extract_text : to retrieve all the text from a XML node. It aggregates text from the node and the child node of its.
- look_for_links : to retrieve every links from a XML node. Looks for each the 'ptr' markup and check if the value of the attribut 'target' starts with 'http' if yes add it to a list and search in child nodes.
- count_figure : count every link in the processed file following these steps

1) Extract the text with extract_text function
2) separate it in words when encountering one of these .;,_ \n()\"" or space
3) check if the word is 'fig' or 'figure' 
4) capture the word behind it
5) if it's a number compare it with the current number and if it's higher then replace it
6) if it's not just pass to the next word
7) iterate over each pdf and draw the visualization

# Wordcloud
- Extract the text from the abstract with extract_text function
- separate it in words when encountering one of these .;,_ \n()\"" or space
- count each word occurrence in a dictionary 
- create the wordcloud from the dictionary using WordCloud library
- verified by looking at the dictionary values and the text printed by extract_text function

# Visualization
- call the count_figure from utils for each file of the output directory
- verified by comparing with the number of figures in the original document (doesn't work for pdf3 but the problem comes from grobid)

# Link list 
- Use the look_for_link function to do a list of link from the markup 'ptr'
- extract the text and look for words which begin by 'http'
- add these words to the list 
- verified by looking for the number of links in the processed file and compare it with the len of the list
